# API

This API is better documented in `/swagger` and `redoc/`

## Endpoints

Two endpoints were defined:

### POST /api/machine_runtime/
```json
{
    "machine_id":   "integer",
    "date":         "string <date>"
}
```

### GET /api/sensor_data

#### Query params:
```json
{
    "page_size":  "integer",
    "page":       "integer",
    "start_date": "string <date>",
    "end_date":   "string <date>",
    "sensors":    "Array[int32]"
}
```

- `page_size` (optional): The number of sensor data points to return per page. Default: 10, maximum: 3000.

- `page` (optional): The page number to retrieve. Default: 1.

- `sensors` (required): A comma-separated list of sensor IDs to filter by. Maximum: 16 sensor IDs.

- `start_date` (required): The start date for the time range filter in the format YYYY-MM-DD.

- `end_date` (required): The end date for the time range filter in the format YYYY-MM-DD.

#### Response

A paginated list of sensor data objects with the following fields:

- `vibration`: The vibration level of the sensor data.

- `date`: The date and time of the sensor data.

- `sensor`: The ID of the sensor.

- `machine`: The ID of the machine associated with the sensor.

#### Example

```json
{
  "count": 123,
  "next": "http://example.com/sensor-data/?page=2",
  "previous": null,
  "results": [
    {
      "vibration": 12.3,
      "date": "2022-01-01T12:00:00Z",
      "sensor": 1,
      "machine": 1
    },
    ...
  ]
}
```

#### Error Response

- 400 Bad Request: The request parameters are invalid or malformed.
- 404 Not Found: No sensor data was found for the provided parameters.

#### Example Request

```bash
curl -X 'GET' \
  'http://localhost:8000/api/sensor_data?page_size=3&page=1&start_date=2023-01-30&end_date=2024-01-30&sensors=3348,2363,2371,3356,3346' \
  -H 'accept: application/json' \
  -H 'X-CSRFToken: 8WL6CY8pRvIaKvAtJtf2ja3a210i5aq9ZkcNSwv0YE5HVe4aTnffoclnFubUCTef'
```

#### Example Response

```json
{
  "count": 3469,
  "next": "http://localhost:8000/api/sensor_data?end_date=2024-01-30&page=2&page_size=3&sensors=3348%2C2363%2C2371%2C3356%2C3346&start_date=2023-01-30",
  "previous": null,
  "results": [
    {
      "vibration": 0.19891693082197517,
      "date": "2024-01-20T00:06:52Z",
      "sensor": 3346,
      "machine": 3338
    },
    {
      "vibration": 0.24213173553819678,
      "date": "2024-01-20T00:06:52Z",
      "sensor": 3348,
      "machine": 3338
    },
    {
      "vibration": 0.2469442080363283,
      "date": "2024-01-20T00:06:52Z",
      "sensor": 3356,
      "machine": 3338
    }
  ]
}
```