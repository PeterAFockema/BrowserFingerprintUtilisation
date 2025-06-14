# nginx image as the base image
FROM nginx:alpine
COPY . /usr/share/nginx/html
# Expose the port 80
EXPOSE 80
# Start nginx when container begins
CMD ["nginx", "-g", "daemon off;"]
