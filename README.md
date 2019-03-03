## ZERO OCR backend
### purpose
This is the core of the project **OCR**. By this I want to gain proficiency in the following aspects.
- Convert given image (scanned image using NN) to text.
- Log the requests for errors, debugging, analytics(**Logging**).
- Write tests to make *sure* of the speed and delivery for customers(**Testing**).

### Logging
Log every request to csv so that it easy import with pandas and visualize. Let there be a request made with an image.
- Log info `Time`-`IPaddress`-`ImageSize`-`ResponseTime`-`Status(200,400,500)`.
- Log error if status is `400` or `500` and save image with `Time`'s epoch seconds.

### Testing
- Tests before deployment.
  - Can deliver a test image with `200`.
- Tests for performance.
  - Check number of parallel connections supported
  - Check number of requests per minute

deployed at [zerocr.herokuapp.com](http://zerocr.herokuapp.com)

frontend code: [ocr_frontned](https://github.com/bharat0to/ocr_frontend)