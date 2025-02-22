#ifndef sondedump_data_h
#define sondedump_data_h

#include <time.h>
#include <stdint.h>

typedef enum {
	PROCEED,
	PARSED
} ParserStatus;


typedef enum {
	SOURCE_END,             /* Samples source exhausted, no more data left */
	FRAME_END,              /* End of this frame, start of the next */
	EMPTY,                  /* No data */
	UNKNOWN,                /* Unknown subframe format */
	INFO,                   /* Generic info (serial nr, burstkill...) */
	POSITION,               /* GPS position and velocity */
	DATETIME,               /* GPS date and time */
	PTU,                    /* Sensor data */
	XDATA,                  /* XDATA */
} DataType;

typedef struct {
	char *sonde_serial;   /* Sonde serial number */
	char *board_model;    /* Board model */
	char *board_serial;   /* Board serial number */

	int seq;                /* Frame sequence number */
	int burstkill_status;   /* -1 if not active, > 0 if active (seconds left) */
} SondeInfo;

typedef struct {
	float lat, lon, alt;
	float speed, heading, climb;
} SondePosition;

typedef struct {
	time_t datetime;
} SondeDateTime;

typedef struct {
	int calibrated;         /* 0 if uncalibrated, nonzero otherwise */
	float calib_percent;    /* Calibration percentage, 0-100 */
	float temp;             /* Temperature, degrees Celsius */
	float rh;               /* Relative humidity % */
	float pressure;         /* Pressure, mbar */
} SondePTU;

typedef struct {
	char *data;
} SondeXDATA;

typedef struct {
	DataType type;
	union {
		SondeInfo info;
		SondePosition pos;
		SondePTU ptu;
		SondeDateTime datetime;
		SondeXDATA xdata;
	} data;
} SondeData;

typedef struct {
	int seq;
	float lat, lon, alt;
	float speed, heading, climb;
	float temp, rh, pressure;
	time_t utc_time;
	int shutdown_timer;
	char serial[32];
	char xdata[128];
	int calibrated;
	float calib_percent;
} PrintableData;
#endif
