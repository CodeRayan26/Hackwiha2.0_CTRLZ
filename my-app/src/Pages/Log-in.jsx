import React from 'react';
import '../css/signup.css'; // Make sure to import the CSS file
import { Link } from 'react-router-dom';

export default function SignUp() {
  return (
    <div className="signup-container">
      <div className="slogan-section">
        <h1 className="slogan-text">
          Powered by <span className="highlight-text">Passion</span>.<br />
          Driven by <span className="highlight-text">Knowledge</span>.
        </h1>
      </div>

      <div className="form-section">
        <form className="form-container">
          <h2 className="form-title">Connect to your account</h2>

          <input
            type="email"
            placeholder="Email"
            className="input-field"
          />
          <input
            type="password"
            placeholder="Password"
            className="input-field"
          />

          <button
            type="submit"
            className="submit-button"
          >
            Log In
          </button>

          <p className="login-link">
            Don't have an account? <a href="/signup" className="login-text">Sign Up</a>
          </p>
        </form>
      </div>
    </div>
  );
}
