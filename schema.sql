-- Database creation
CREATE DATABASE IF NOT EXISTS learning_platform;
USE learning_platform;

-- ======================
-- CORE TABLES
-- ======================

-- Users table (base table for all users)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    account_type ENUM('free', 'premium') NOT NULL DEFAULT 'free',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_account_type (account_type)
) ENGINE=InnoDB;

-- ======================
-- CREATOR TABLES (FREE CONTENT)
-- ======================

-- Creators table (for free content creators)
CREATE TABLE creators (
    creator_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    nin_number VARCHAR(50) NOT NULL COMMENT 'National Identification Number',
    id_card_front_url VARCHAR(255) NOT NULL,
    id_card_back_url VARCHAR(255),
    specialty VARCHAR(100) NOT NULL,
    specialty_proof_url VARCHAR(255),
    is_verified BOOLEAN DEFAULT FALSE,
    verification_date TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_creator_verified (is_verified)
) ENGINE=InnoDB;

-- Feed content (free content from creators)
CREATE TABLE feed_content (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    creator_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    content_type ENUM('post', 'mini_course', 'full_course') NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (creator_id) REFERENCES creators(creator_id) ON DELETE CASCADE,
    INDEX idx_feed_content_type (content_type)
) ENGINE=InnoDB;

-- Feed content media
CREATE TABLE feed_media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    content_id INT NOT NULL,
    media_url VARCHAR(255) NOT NULL,
    media_type ENUM('image', 'video', 'document', 'audio') NOT NULL,
    display_order INT DEFAULT 0,
    FOREIGN KEY (content_id) REFERENCES feed_content(content_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ======================
-- PROFESSIONAL TABLES (PREMIUM CONTENT)
-- ======================

-- Professionals table (verified experts)
CREATE TABLE professionals (
    professional_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    diploma_url VARCHAR(255) NOT NULL,
    diploma_issuer VARCHAR(100) NOT NULL,
    certification_url VARCHAR(255),
    years_experience INT,
    specialty VARCHAR(100) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_date TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_pro_verified (is_verified)
) ENGINE=InnoDB;

-- Professional subscription plans (prm1, prm2, prm3)
CREATE TABLE professional_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    professional_id INT NOT NULL,
    plan_type ENUM('prm1', 'prm2', 'prm3') NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    duration_days INT NOT NULL COMMENT '30=monthly, 365=yearly',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_pro_plan (professional_id, plan_type),
    FOREIGN KEY (professional_id) REFERENCES professionals(professional_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Professional content (premium content)
CREATE TABLE pro_content (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    professional_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    full_content TEXT NOT NULL,
    preview_content TEXT COMMENT 'Free preview content',
    content_type ENUM('course', 'coaching', 'mentorship') NOT NULL,
    price DECIMAL(10,2) COMMENT 'NULL means included in subscription',
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_id) REFERENCES professionals(professional_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Content access levels (which plans get which content)
CREATE TABLE content_access_levels (
    content_id INT NOT NULL,
    plan_id INT NOT NULL,
    PRIMARY KEY (content_id, plan_id),
    FOREIGN KEY (content_id) REFERENCES pro_content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES professional_plans(plan_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ======================
-- COMMON TABLES
-- ======================

-- Categories (for both feed and pro content)
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    applies_to ENUM('feed', 'pro', 'both') NOT NULL DEFAULT 'both'
) ENGINE=InnoDB;

-- Feed content categories
CREATE TABLE feed_content_categories (
    content_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (content_id, category_id),
    FOREIGN KEY (content_id) REFERENCES feed_content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Pro content categories
CREATE TABLE pro_content_categories (
    content_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (content_id, category_id),
    FOREIGN KEY (content_id) REFERENCES pro_content(content_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- User subscriptions to professional plans
CREATE TABLE user_subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(255),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES professional_plans(plan_id)
) ENGINE=InnoDB;

-- ======================
-- SAMPLE DATA
-- ======================

-- Insert sample users
INSERT INTO users (username, email, password_hash, account_type) VALUES
('learner1', 'learner1@example.com', '$2a$10$hashed1', 'free'),
('creator1', 'creator1@example.com', '$2a$10$hashed2', 'free'),
('pro1', 'pro1@example.com', '$2a$10$hashed3', 'premium');

-- Insert sample creator
INSERT INTO creators (user_id, nin_number, id_card_front_url, specialty, is_verified) VALUES
(2, 'NIN123456', 'https://example.com/id1.jpg', 'Graphic Design', TRUE);

-- Insert sample professional
INSERT INTO professionals (user_id, diploma_url, diploma_issuer, certification_url, is_verified ,specialty ) VALUES
(3, 'https://example.com/diploma1.pdf', 'Stanford', 'https://example.com/cert1.pdf', TRUE , specialty);

-- Insert sample feed content
INSERT INTO feed_content (creator_id, title, content, content_type) VALUES
(1, 'Design Basics', 'Learn fundamental design principles...', 'mini_course'),
(1, 'Color Theory', 'Understanding color combinations...', 'post');

-- Insert sample professional plans
INSERT INTO professional_plans (professional_id, plan_type, name, description, price, duration_days) VALUES
(1, 'prm1', 'Starter', 'Basic courses', 9.99, 30),
(1, 'prm2', 'Professional', 'All courses', 29.99, 30),
(1, 'prm3', 'VIP', 'Courses + coaching', 99.99, 30);

-- Insert sample pro content
INSERT INTO pro_content (professional_id, title, description, full_content, content_type) VALUES
(1, 'Advanced UX', 'Master UX design', 'Full course content...', 'course'),
(1, '1-on-1 Coaching', 'Personalized guidance', 'Coaching details...', 'coaching');

-- Assign content to plans
INSERT INTO content_access_levels (content_id, plan_id) VALUES
(1, 1), -- Starter gets course 1
(1, 2), (2, 2), -- Professional gets both
(1, 3), (2, 3); -- VIP gets everything

-- Insert categories
INSERT INTO categories (name, applies_to) VALUES
('Design', 'both'),
('Business', 'both'),
('Premium Skills', 'pro');

-- Categorize content
INSERT INTO feed_content_categories (content_id, category_id) VALUES
(1, 1), (2, 1); -- Both feed posts are Design

INSERT INTO pro_content_categories (content_id, category_id) VALUES
(1, 1), -- UX course is Design
(1, 3); -- UX course is also Premium Skills

-- ======================
-- KEY RELATIONSHIPS
-- ======================
/*
1. Users can be:
   - Regular learners (account_type = 'free')
   - Creators (has record in creators table)
   - Professionals (has record in professionals table)

2. Content flows:
   - Free content: users → creators → feed_content
   - Premium content: users → professionals → pro_content → professional_plans

3. Access control:
   - Free content: available to all
   - Pro content: requires subscription to matching plan
*/
ALTER TABLE creators
ADD COLUMN level int default 0, 
Add column points int default 0