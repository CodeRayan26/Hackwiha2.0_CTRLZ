import "../css/mainpage.css"

function MainPage() {
  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="logo-container">
          <div className="logo">
            <svg className="cap-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M12 3L1 9l11 6l9-4.91V17h2V9L12 3z" />
              <path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z" />
            </svg>
          </div>
          <h1 className="logo-text">Name</h1>
        </div>

        <div className="search-container">
          <svg className="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 0 0 1.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 0 0-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 0 0 5.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
          </svg>
          <input type="text" placeholder="Search" className="search-input" />
        </div>

        <div className="nav-container">
          <div className="dropdown">
            <button className="dropdown-button">
              Pro <span className="dropdown-arrow">▼</span>
            </button>
          </div>
          <a href="#about" className="nav-link">
            About Us
          </a>
          <a href="#contact" className="nav-link">
            Contact Us
          </a>
          <div className="profile-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z" />
            </svg>
          </div>
        </div>
      </header>

      {/* Category Filters */}
      <div className="category-filters">
        <button className="category-button">All</button>
        <button className="category-button">Algorithms</button>
        <button className="category-button">Philosophy</button>
        <button className="category-button">Statistics</button>
        <button className="category-button">Logic</button>
        <button className="category-button">Physics</button>
        <button className="category-button">Psychology</button>
        <button className="category-button">Chemistry</button>
        <button className="category-button">Geometry</button>
      </div>

      {/* Main Content */}
      <main className="main-content">
        <div className="sidebar">
          <h2 className="sidebar-title">Top Pros of the Week</h2>
          <div className="pro-list">
            <div className="pro-item">
              <img src="/placeholder.svg?height=50&width=50" alt="Tyler H" className="pro-avatar" />
              <span className="pro-name">Tyler .H</span>
            </div>
            <div className="pro-item">
              <img src="/placeholder.svg?height=50&width=50" alt="Maria K" className="pro-avatar" />
              <span className="pro-name">Maria .K</span>
            </div>
            <div className="pro-item">
              <img src="/placeholder.svg?height=50&width=50" alt="Lynda R" className="pro-avatar" />
              <span className="pro-name">Lynda .R</span>
            </div>
            <div className="pro-item">
              <img src="/placeholder.svg?height=50&width=50" alt="Mohamed P" className="pro-avatar" />
              <span className="pro-name">Mohamed .P</span>
            </div>
            <div className="pro-item">
              <img src="/placeholder.svg?height=50&width=50" alt="Chahrazed B" className="pro-avatar" />
              <span className="pro-name">Chahrazed .B</span>
            </div>
          </div>
        </div>

        <div className="content">
          <div className="intro-section">
            <h2 className="intro-title">Ready to Level Up?</h2>
            <p className="intro-text">
              Our Pros are here to take your skills to the next level—with expert content, mentorship, and more.
            </p>
          </div>

          {/* Pro Cards */}
          <div className="pro-cards">
            {/* Tyler's Card */}
            <div className="pro-card">
              <div className="pro-card-header">
                <img src="/placeholder.svg?height=60&width=60" alt="Tyler H" className="pro-card-avatar" />
                <div className="pro-card-title">
                  <h3 className="pro-card-name">Tyler .H</h3>
                  <span className="pro-badge">Pro</span>
                </div>
                <div className="pro-card-actions">
                  <button className="favorite-button">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="heart-icon">
                      <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                    </svg>
                  </button>
                  <button className="profile-button">See Profile</button>
                </div>
              </div>
              <div className="pro-card-body">
                <p className="pro-research">Research in Algorithmic Complexity and Optimization</p>
                <div className="pro-tags">
                  <span className="pro-tag">Algorithms</span>
                  <span className="pro-tag">Data Structures</span>
                  <span className="pro-tag">Computer Science</span>
                </div>
              </div>
              <div className="pro-card-footer">
                <span className="pro-price">From 7000DZD</span>
              </div>
            </div>

            {/* Maria's Card */}
            <div className="pro-card">
              <div className="pro-card-header">
                <img src="/placeholder.svg?height=60&width=60" alt="Maria K" className="pro-card-avatar" />
                <div className="pro-card-title">
                  <h3 className="pro-card-name">Maria .K</h3>
                  <span className="pro-badge">Pro</span>
                </div>
                <div className="pro-card-actions">
                  <button className="favorite-button">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="heart-icon">
                      <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                    </svg>
                  </button>
                  <button className="profile-button">See Profile</button>
                </div>
              </div>
              <div className="pro-card-body">
                <p className="pro-research">Research in Linear Algebra and Matrix Theory</p>
                <div className="pro-tags">
                  <span className="pro-tag">Algebra</span>
                  <span className="pro-tag">Linear Algebra</span>
                </div>
              </div>
              <div className="pro-card-footer">
                <span className="pro-price">From 6000DZD</span>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-links">
            <a href="#about" className="footer-link">
              About Us
            </a>
            <a href="#why" className="footer-link">
              Why Us
            </a>
            <a href="#contact" className="footer-link">
              Contact Us
            </a>
          </div>

          <div className="footer-social">
            <a href="#" className="social-link facebook">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="social-icon">
                <path d="M12 2C6.477 2 2 6.477 2 12c0 5.013 3.693 9.153 8.505 9.876V14.65H8.031v-2.629h2.474v-1.749c0-2.896 1.411-4.167 3.818-4.167 1.153 0 1.762.085 2.051.124v2.294h-1.642c-1.022 0-1.379.969-1.379 2.061v1.437h2.995l-.406 2.629h-2.588v7.247C18.235 21.236 22 17.062 22 12c0-5.523-4.477-10-10-10z" />
              </svg>
            </a>
            <a href="#" className="social-link twitter">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="social-icon">
                <path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z" />
              </svg>
            </a>
            <a href="#" className="social-link linkedin">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="social-icon">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z" />
              </svg>
            </a>
          </div>

          <div className="footer-contact">
            <div className="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="contact-icon">
                <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
              </svg>
              <span>name-contact@gmail.com</span>
            </div>
            <div className="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="contact-icon">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z" />
              </svg>
              <span>+213-***-***-***</span>
            </div>
            <div className="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="contact-icon">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
              </svg>
              <span>1 Rue jsp , Algeries, Algeria</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default MainPage
