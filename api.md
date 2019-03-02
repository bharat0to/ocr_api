## OCR api

> POST /scan

Input format
- Headers
  - Content-Type: application/json
```
    {
        "data": <base64>
    }
```
Output

    {
        "text": <scanned text>
    }
