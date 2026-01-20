# Get the nodejs version 22 from the docker hub
FROM node:22-alpine

# Set working directory
WORKDIR /app


# Copy package.json and package-lock.json to the working directory
# `*` means to pick package.json and package-lock.json
# `./` means to get the files from the current (root) directory
COPY package*.json ./


# Install dependencies based on the preferred package manager
RUN npm install

# Copy the rest of the application codebase from current directory to WORKDIR /app
COPY . .

# Build the app
RUN npm run build

# Expose port on which the app will run
EXPOSE 3000

# Run the app
CMD ["npm", "start"]