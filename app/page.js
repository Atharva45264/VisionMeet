"use client"

import { useState } from "react";

export default function Home() {
  useState("");
  return (
    <div className="flex items-center justify-center min-h-screen bg-linear-to-br from-gray-900 via-gray-800 to-gray-900 text-white">
      <div className= "p-8 bg-gray-800/60 rounded-2xl border border-gray-700 w-80 shadow-2xl">
      <h2 className="text-xl font-semibold mb-4 text-center">Enter your Name</h2>

      <input className="px-4 py-3 w-full rounded-lg bg-gray-700/80 border border-gray-600 text-white"/>
      </div>
    </div>
  );
}
