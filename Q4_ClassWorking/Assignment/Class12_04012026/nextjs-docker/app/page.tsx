import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Image
              src="/next.svg"
              alt="Next.js Logo"
              width={120}
              height={24}
              priority
            />
            <span className="text-lg font-semibold text-gray-600">+</span>
            <div className="flex items-center space-x-1">
              <div className="w-6 h-6 bg-blue-500 rounded-full"></div>
              <span className="font-bold text-blue-600">Docker</span>
            </div>
          </div>
          <nav>
            <ul className="flex space-x-6">
              <li><a href="#" className="text-gray-600 hover:text-blue-600 transition">Home</a></li>
              <li><a href="#" className="text-gray-600 hover:text-blue-600 transition">Docs</a></li>
              <li><a href="#" className="text-gray-600 hover:text-blue-600 transition">Deploy</a></li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-grow container mx-auto px-4 py-12 flex flex-col items-center">
        <div className="max-w-4xl text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-800 mb-6">
            Next.js App Containerized with <span className="text-blue-600">Docker</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            This is a modern Next.js application packaged and deployed using Docker containers.
            Experience the power of containerization with the flexibility of Next.js.
          </p>

          <div className="bg-white rounded-xl shadow-lg p-8 mb-12 inline-block">
            <div className="flex items-center justify-center space-x-4 mb-4">
              <div className="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center">
                <span className="text-white font-bold">N</span>
              </div>
              <div className="text-3xl">+</div>
              <div className="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center">
                <span className="text-white font-bold">D</span>
              </div>
            </div>
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">Containerized Success!</h2>
            <p className="text-gray-600 mb-6">
              Your Next.js application is now running inside a Docker container.
            </p>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-5xl mb-16">
          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
              </svg>
            </div>
            <h3 className="text-xl font-semibold text-gray-800 mb-2">Containerized</h3>
            <p className="text-gray-600">
              Built and deployed using Docker containers for consistent environments.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 className="text-xl font-semibold text-gray-800 mb-2">Fast & Scalable</h3>
            <p className="text-gray-600">
              Optimized for performance with Next.js 15 and modern web standards.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
              </svg>
            </div>
            <h3 className="text-xl font-semibold text-gray-800 mb-2">Ready to Deploy</h3>
            <p className="text-gray-600">
              Easily deploy to any cloud platform supporting Docker containers.
            </p>
          </div>
        </div>

        {/* Quick Start */}
        <div className="bg-white rounded-lg shadow-md p-8 w-full max-w-3xl">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">Quick Start with Docker</h2>
          <div className="space-y-4">
            <div className="flex items-center space-x-4">
              <span className="bg-gray-800 text-white px-3 py-1 rounded font-mono text-sm">#1</span>
              <code className="bg-gray-100 text-gray-800 px-4 py-2 rounded font-mono text-sm flex-grow">
                docker build -t nextjs-docker .
              </code>
            </div>
            <div className="flex items-center space-x-4">
              <span className="bg-gray-800 text-white px-3 py-1 rounded font-mono text-sm">#2</span>
              <code className="bg-gray-100 text-gray-800 px-4 py-2 rounded font-mono text-sm flex-grow">
                docker run -p 3000:3000 nextjs-docker
              </code>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8">
        <div className="container mx-auto px-4 text-center">
          <p className="mb-2">Next.js + Docker Application</p>
          <p className="text-gray-400 text-sm">Built with modern web technologies</p>
        </div>
      </footer>
    </div>
  );
}
