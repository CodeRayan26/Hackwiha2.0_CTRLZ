import React from 'react';
import '../css/landing.css';
import { Link } from 'react-router-dom';


export default function Landing() {
  return (
    <div className="app-container">
      {/* Navigation Bar */}
      <header className="header">
        <div className="header-left">
          <div className="logo-container">
            <div className="logo-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" className="icon">
                <path d="M11.7 2.805a.75.75 0 01.6 0A60.65 60.65 0 0122.83 8.72a.75.75 0 01-.231 1.337 49.949 49.949 0 00-9.902 3.912l-.003.002-.34.18a.75.75 0 01-.707 0A50.009 50.009 0 007.5 12.174v-.224c0-.131.067-.248.172-.311a54.614 54.614 0 014.653-2.52.75.75 0 00-.65-1.352 56.129 56.129 0 00-4.78 2.589 1.858 1.858 0 00-.859 1.228 49.803 49.803 0 00-4.634-1.527.75.75 0 01-.231-1.337A60.653 60.653 0 0111.7 2.805z" />
                <path d="M13.06 15.473a48.45 48.45 0 017.666-3.282c.134 1.414.22 2.843.255 4.285a.75.75 0 01-.46.71 47.878 47.878 0 00-8.105 4.342.75.75 0 01-.832 0 47.877 47.877 0 00-8.104-4.342.75.75 0 01-.461-.71c.035-1.442.121-2.87.255-4.286A48.4 48.4 0 016 13.18v1.27a1.5 1.5 0 00-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.661a6.729 6.729 0 00.551-1.608 1.5 1.5 0 00.14-2.67v-.645a48.549 48.549 0 013.44 1.668 2.25 2.25 0 002.12 0z" />
                <path d="M4.462 19.462c.42-.419.753-.89 1-1.394.453.213.902.434 1.347.661a6.743 6.743 0 01-1.286 1.794.75.75 0 11-1.06-1.06z" />
              </svg>
            </div>
            <span className="logo-text">ProPath</span>
          </div>
          <div className="search-container">
            <svg className="search-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="text" placeholder="Search" className="search-input" />
          </div>
        </div>
        <div className="header-right">
          <div className="dropdown">
            <button className="dropdown-button">
              Free
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="dropdown-icon"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>
          <a href="/about" className="nav-link">About Us</a>
          <a href="/contact" className="nav-link">Contact Us</a>
          <Link to='/Sign-up'><button className="get-started-button">Get Started</button></Link>
        </div>
      </header>

      <main className="main-content">
        {/* Hero Section */}
        <section className="hero-section">
          <div className="container hero-container">
            <div className="hero-image-container">
              <img src="/placeholder.svg?height=400&width=500" alt="Student learning" className="hero-image" />
            </div>
            <div className="hero-content">
              <h1 className="hero-title">
                Two paths, one mission<br />helping you grow.
              </h1>
              <p className="hero-subtitle">Empowering your learning journey, every step of the way.</p>
              <button className="hero-button">Get Started</button>
            </div>
          </div>
        </section>

        {/* Categories */}
        <section className="categories-section">
          <div className="container">
            <div className="categories-container">
              {['All', 'Algorithms', 'Philosophy', 'Statistics', 'Logic', 'Physics', 'Psychology', 'Chemistry', 'Geometry', 'Calculus'].map((category) => (
                <button key={category} className="category-button">
                  {category}
                </button>
              ))}
            </div>
          </div>
        </section>

        {/* Popular Courses */}
        <section className="courses-section">
          <div className="container">
            <h2 className="section-title">Our Popular Courses</h2>
            
            <div className="courses-grid">
              {/* Course 1 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Differential Equations" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Mastery of Differential Equations</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Advanced</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">150 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">4</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Course 2 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Logic and Philosophy" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Logic and Philosophical Argumentation</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Intermediate</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">120 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">13</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Course 3 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Algorithms" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Foundations of Algorithms</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Beginner</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">130 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">78</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Course 4 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Quantum Mechanics" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Basics of Quantum Mechanics</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Intermediate</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">200 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">24</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Course 5 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Statistical Analysis" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Introduction to Statistical Analysis</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Beginner</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">180 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">30</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Course 6 */}
              <div className="course-card">
                <div className="course-content">
                  <div className="course-image-container">
                    <img src="/placeholder.svg?height=150&width=150" alt="Organic Chemistry" className="course-image" />
                  </div>
                  <div className="course-details">
                    <h3 className="course-title">Organic Chemistry Essentials</h3>
                    <div className="course-info">
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">Advanced</span>
                      </div>
                      <div className="info-item">
                        <div className="radio-dot"><div className="radio-dot-inner"></div></div>
                        <span className="info-text">90 hours</span>
                      </div>
                      <div className="info-item">
                        <div className="star-rating">
                          <svg xmlns="http://www.w3.org/2000/svg" className="star-icon" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </div>
                        <span className="info-text">47</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* About Us */}
        <section className="about-section">
          <div className="container">
            <h2 className="section-title">About Us</h2>
            
            <div className="about-container">
              <div className="about-sidebar">
                <div className="about-sidebar-content">
                  <h3 className="about-sidebar-title">Who We Are?</h3>
                </div>
              </div>
              <div className="about-content">
                <p className="about-text">
                  At [Platform Name], we believe education should be both accessible and high-quality. That's why we've created a two-tiered learning ecosystem designed to connect learners with verified experts and passionate emerging educators.
                </p>
                <p className="about-text">
                  Our platform empowers users to choose their own learning path – whether it's guided by a certified professional ("Pro") or discovered through the creativity and innovation of new voices ("Creators") on the learning feed.
                </p>
                <p className="about-text">
                  We're building more than just a course platform – we're cultivating a community where knowledge flows freely, talent is recognized, and learning never stops.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="footer-nav">
              <nav className="footer-links">
                <a href="/about" className="footer-link">About Us</a>
                <a href="/why-us" className="footer-link">Why Us</a>
                <a href="/contact" className="footer-link">Contact Us</a>
              </nav>
            </div>
            <div className="footer-contact">
              <div className="contact-item">
                <svg className="contact-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
                <span>name-contact@gmail.com</span>
              </div>
              <div className="contact-item">
                <svg className="contact-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
                <span>+213-***-***-***</span>
              </div>
              <div className="contact-item">
                <svg className="contact-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>1 Rue rpp , Algeries, Algeria</span>
              </div>
            </div>
          </div>
          <div className="footer-social">
            <a href="#" className="social-link facebook">
              <svg xmlns="http://www.w3.org/2000/svg" className="social-icon" fill="currentColor" viewBox="0 0 24 24">
                <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z" />
              </svg>
            </a>
            <a href="#" className="social-link twitter">
              <svg xmlns="http://www.w3.org/2000/svg" className="social-icon" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
              </svg>
            </a>
            <a href="#" className="social-link linkedin">
              <svg xmlns="http://www.w3.org/2000/svg" className="social-icon" fill="currentColor" viewBox="0 0 24 24">
                <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z" />
              </svg>
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
