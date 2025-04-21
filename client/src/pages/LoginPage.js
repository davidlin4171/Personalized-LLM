import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (email.trim() === "" || password.trim() === "") {
      alert("Please enter correct email address and password");
      return;
    }
    localStorage.setItem("user", JSON.stringify({ email }));

    // TODO: Call backend API to verify user credentials

    console.log("Logging in", email, password);
    navigate("/chat");
  };

  return (
    <div className="min-h-screen flex justify-center items-start pt-24 bg-gray-100">
      <div className="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6 text-center">Sign In</h2>
        <div className="space-y-4">
          <input
            type="email"
            className="w-full px-4 py-2 border border-gray-300 rounded"
            placeholder=""
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            className="w-full px-4 py-2 border border-gray-300 rounded"
            placeholder=""
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button
            onClick={handleLogin}
            className="w-full py-2 bg-black text-white rounded hover:bg-gray"
          >
            Sign In
          </button>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
