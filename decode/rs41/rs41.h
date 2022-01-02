#ifndef rs41_h
#define rs41_h

#include "decode/common.h"
#include "decode/correlator/correlator.h"
#include "decode/ecc/rs.h"
#include "demod/gfsk.h"
#include "protocol.h"

typedef struct {
	int initialized;
	RS41Calibration data;
	uint8_t missing[sizeof(RS41Calibration)/8/RS41_CALIB_FRAGSIZE+1];
} RS41Metadata;

typedef struct {
	GFSKDemod gfsk;
	Correlator correlator;
	RSDecoder rs;
	RS41Frame frame[2];
	int state;
	int offset, frame_offset;
	int calibrated;
	RS41Metadata metadata;
	float pressure;
	char serial[9];
} RS41Decoder;

/**
 * Initialize a Vaisala RS41 frame decoder
 *
 * @param d decoder to init
 * @param samplerate samplerate of the raw FM-demodulated stream
 */
void rs41_decoder_init(RS41Decoder *d, int samplerate);

/**
 * Deinitialize the given decoder
 *
 * @param d deocder to deinit
 */
void rs41_decoder_deinit(RS41Decoder *d);

/**
 * Decode the next frame in the stream
 *
 * @param d decoder to use
 * @param read function to use to pull in new raw samples
 */
SondeData rs41_decode(RS41Decoder *d, int (*read)(float *dst));

#endif
