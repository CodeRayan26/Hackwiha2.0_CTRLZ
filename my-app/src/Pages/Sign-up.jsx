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
          <h2 className="form-title">Create your account</h2>

          <input
            type="text"
            placeholder="Username"
            className="input-field"
          />
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
            Sign Up
          </button>

          <p className="login-link">
            Already have an account? <a href="/login" className="login-text">Log in</a>
          </p>
        </form>
      </div>
    </div>
  );
}
