# Use an official Nginx image to serve static files
FROM nginx:alpine

# Copy the frontend static files and HTML templates into the container
COPY ./static /usr/share/nginx/html/static
COPY ./templates /usr/share/nginx/html/templates

# Expose the Nginx default port
EXPOSE 80
