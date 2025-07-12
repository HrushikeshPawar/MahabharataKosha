# Use the official Node.js 20 Alpine image as a base
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package.json and pnpm-lock.yaml (if available)
COPY package.json pnpm-lock.yaml* ./

# Install dependencies using pnpm
RUN pnpm install

# Copy the rest of the application source code
COPY . .

# Expose the port the Vite dev server will run on
EXPOSE 5173

# Run the Vite dev server and make it accessible from outside the container
CMD ["pnpm", "run", "dev", "--host", "0.0.0.0"]
