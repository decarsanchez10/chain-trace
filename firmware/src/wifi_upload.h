#ifndef WIFI_UPLOAD_H
#define WIFI_UPLOAD_H

#include <Arduino.h>

void connectWiFi(const char* ssid, const char* password);
bool postCustodyScan(const String &jsonPayload);

#endif
