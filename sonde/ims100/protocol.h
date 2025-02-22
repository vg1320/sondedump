#ifndef ims100_protocol_h
#define ims100_protocol_h

#include <stdint.h>
#include <math.h>
#include <time.h>
#include "utils.h"

#define IMS100_BAUDRATE 2400

#define IMS100_SYNCWORD 0xaaa56a659a99559a
#define IMS100_SYNC_LEN 8
#define IMS100_FRAME_LEN 1200

#define IMS100_SUBFRAME_LEN 300
#define IMS100_SUBFRAME_BCHLEN 12
#define IMS100_SUBFRAME_VALUELEN 17
#define IMS100_MESSAGE_LEN (2 * IMS100_SUBFRAME_VALUELEN + IMS100_SUBFRAME_BCHLEN)

#define IMS100_REEDSOLOMON_N 63
#define IMS100_REEDSOLOMON_K 51
#define IMS100_REEDSOLOMON_T 4
#define IMS100_REEDSOLOMON_POLY 0x61

#define IMS100_DATA_VALID(bits, mask) (((bits) & (mask)) == (mask))

#define IMS100_GPS_MASK_SPEED   0x000002
#define IMS100_GPS_MASK_HEADING 0x000004
#define IMS100_GPS_MASK_ALT     0x000060
#define IMS100_GPS_MASK_LON     0x000180
#define IMS100_GPS_MASK_LAT     0x000600
#define IMS100_GPS_MASK_DATE    0x000800
#define IMS100_GPS_MASK_TIME    0x003000

#define IMS100_MASK_SEQ     0x800000
#define IMS100_MASK_CALIB   0x180000
#define IMS100_MASK_SUBTYPE 0x020000
#define IMS100_MASK_PTU     0x00FC00

#define IMS100_SUBTYPE_GPS  0x30c1
#define IMS100_SUBTYPE_META 0x31c1

#define IMS100_CALIB_PTU_MASK   0x0000FFFFFFFFFFFF
#define IMS100_CALIB_SERIAL_MASK   0x8000000000000000

#define IMS100_CALIB_FRAGSIZE 4
#define IMS100_CALIB_FRAGCOUNT 64

static const uint8_t ims100_bch_roots[] = {0x02, 0x04, 0x08, 0x10};

/* Even & odd seq subframe types {{{ */
PACK(typedef struct {
	uint8_t _pad0[4];
	uint8_t ms[2];
	uint8_t hour;
	uint8_t min;

	/* Offset 24 */
	uint8_t date[2];
	uint8_t lat[4];
	uint8_t lon[4];
	uint8_t alt[3];
	uint8_t _pad3[5];
	uint8_t heading[2];
	uint8_t speed[2];
	uint8_t _pad4[2];
}) IMS100FrameGPS;

PACK(typedef struct {
	uint8_t _pad3[10];

	/* Offset 26 */
	uint8_t flags;
	uint8_t fragment_seq;
	uint8_t fragment_data[16];
	uint8_t _pad4[2];
}) IMS100FrameMeta;
/* }}} */

PACK(typedef struct {
	/* Offset 0 */
	uint8_t seq[2];
	uint8_t adc_val0[2];     /* Actual content depends on seq, has period = 4 frames */
	                         /* Seq = 0b..00: ADC reference */
	                         /* Seq = 0b..01: Always zero */
	                         /* Seq = 0b..10: TBD */
	                         /* Seq = 0b..11: RH temperature sensor ADC value */
	uint8_t calib[IMS100_CALIB_FRAGSIZE];
	uint8_t _pad1[2];
	uint8_t adc_val1[2];
	uint8_t adc_val2[2];    /* Actual content depends on seq, has period = 4 frames */
	                        /* Seq = 0b..00, 01, 10: RH sensor ADC value */
	                        /* Seq = 0b..11:         ADC reference */
	uint8_t subtype[2];

	/* Offset 16 */
	union {
		IMS100FrameGPS gps;
		IMS100FrameMeta meta;
	} data;

	uint32_t valid;
}) IMS100Frame;

/* Frame as received, including all the ECC blocks and parity bits */
PACK(typedef struct {
	uint8_t syncword[3];
	uint8_t data[72];
}) IMS100ECCFrame;

PACK(typedef struct {
	uint8_t _pad[2];
	uint8_t serial[4];                  /* Sonde serial number. IEEE754, big endian */
	uint8_t _unk0[64];
	uint8_t temps[12][4];               /* Calibration temperatures, +60..-85'C. IEEE754, big endian */
	uint8_t _unk2[16];
	uint8_t temp_resists[12][4];        /* Thermistor kOhm @ temp. IEEE754, big endian */
	uint8_t _unk3[16];
	uint8_t rh_calib_coeffs[4][4];      /* RH 3rd degree polynomial coefficients. IEEE754, big endian */
	uint8_t temp_calib_coeffs[4][4];    /* Temp 3rd degree polynomial coefficients. IEEE754, big endian*/
	uint8_t rh_temp_calib_coeffs[4][4];
	uint8_t _unk_end[10];
}) IMS100Calibration;

#endif
