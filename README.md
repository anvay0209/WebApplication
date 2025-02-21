# WebApplication
# Image Processor for X

A Streamlit web application that allows users to upload images, automatically resize them to specific dimensions, and post them to X (Twitter).

## Features

- Image upload and validation
- Automatic image resizing with aspect ratio preservation
- Customizable image dimensions
- X (Twitter) integration for posting
- Responsive design that works across devices
- Secure authentication handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-processor-x
cd image-processor-x
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up X API credentials:
Create a `.streamlit/secrets.toml` file with your X API credentials:
```toml
[
twitter_credentials
]
api_key = "your_api_key"
api_secret = "your_api_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
```

## Running Locally

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Deployment

This app can be deployed on Streamlit Cloud:

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your secrets in the Streamlit Cloud dashboard

## Usage

1. Open the app in your browser
2. Upload an image using the file uploader
3. (Optional) Configure custom image sizes in the sidebar
4. Click "Process Images" to generate resized versions
5. Connect your X account
6. Click "Post Images to X" to publish

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

[MIT](https://choosealicense.com/licenses/mit/)
