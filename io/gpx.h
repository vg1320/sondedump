#ifndef gpx_h
#define gpx_h

#include <stdio.h>
#include <time.h>

typedef struct {
	FILE *fd;
	int track_active;
} GPXFile;

int gpx_init(GPXFile *file, char *fname);
void gpx_close(GPXFile *file);
void gpx_start_track(GPXFile *file, char *name);
void gpx_add_trackpoint(GPXFile *file, float lat, float lon, float alt, float spd, float hdg, time_t time);
void gpx_stop_track(GPXFile *file);

#endif
