echo "For Firefox extensions..."

echo "Use npm to install web-ext"
npm install --global web-ext

echo "Confirm version..."
web-ext --version


echo "To build..."
web-ext build
# web-ext build --overwrite-dest

echo "To run..."
web-ext run