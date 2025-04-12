# API Documentation

## Base URL
`http://localhost:8000`

## Authentication
- **Login**: `POST /login`
  - Request: `OAuth2PasswordRequestForm` (username, password)
  - - Response: `{"access_token": "token", "token_type": "bearer"}`
  - Description: Authenticate a user and return a JWT token. -- Response and return will not be implemented to focus on technical backend details and chat system , the fronted dev will only use username and password in the endpoints 

## Channel and Messaging Endpoints
- **Get User Channels**: `GET /chat/users/{user_id}/channels`
  - Response: `List[Channel]`
  - Description: Retrieve all channels a user has access to (authenticated).
- **Get Channel**: `GET /chat/channels/{channel_id}`
  - Response: `ChannelWithMessages`
  - Description: Retrieve a channel and its messages or course content (authenticated, user must have access to the channel).
- **Send Message**: `POST /chat/channels/{channel_id}/messages`
  - Request: `MessageCreate` (content)
  - Response: `Message`
  - Description: Send a message in a group coaching or mentorship channel (authenticated, Professional only).

## User Endpoints
- **Register Learner**: `POST /register/learner`
  - Request: `UserCreate` (username, email, password, account_type)
  - Response: `UserOut`
  - Description: Register a new learner.
- **Register Professional**: `POST /register/professional`
  - Request: `ProfessionalCreate` (username, email, password, account_type, diploma_url, diploma_issuer, certification_url, years_experience, specialty)
  - Response: `UserOut`
  - Description: Register a new professional.
- **Get User Profile**: `GET /users/{user_id}`
  - Response: `UserOut`
  - Description: Retrieve a user's profile.
- **Update User Profile**: `PUT /users/{user_id}/profile`
  - Request: `UserUpdate` (username, email, account_type, password)
  - Response: `UserOut`
  - Description: Update a user's profile (authenticated).

## Creator Endpoints
- **Become Creator**: `POST /users/{user_id}/become_creator`
  - Request: `LearnerToCreator` (nin_number, id_card_front_url, id_card_back_url, specialty)
  - Response: `UserOut`
  - Description: Promote a user to a Creator.
- **Get Creator Profile**: `GET /creators/{creator_id}/profile`
  - Response: `CreatorProfile`
  - Description: Retrieve a Creator's profile with their feed content.
- **Promote to Pro (Admin)**: `POST /admin/creators/{creator_id}/promote-to-pro`
  - Response: `UserOut`
  - Description: Promote a Creator to a Pro (admin function for MVP).

## Feed Endpoints
- **Create Feed Content**: `POST /feed`
  - Request: `FeedContentCreate` (title, content, content_type, is_featured)
  - Response: `FeedContent`
  - Description: Create a new feed content item (authenticated, creator only).
- **Get Feed**: `GET /feed?sort=recent`
  - Response: `List[FeedContentWithMedia]`
  - Description: Retrieve the feed, sorted by most recent.
- **Get Feed Content**: `GET /feed/{content_id}`
  - Response: `FeedContentWithMedia`
  - Description: Retrieve a specific feed content item with its media.
- **Create Feed Media**: `POST /feed/{content_id}/media`
  - Request: `FeedMediaCreate` (media_url, media_type, display_order)
  - Response: `FeedMedia`
  - Description: Add media to a feed content item (authenticated).
- **Update Feed Media**: `PUT /feed/media/{media_id}`
  - Request: `FeedMediaCreate`
  - Response: `FeedMedia`
  - Description: Update a feed media item (authenticated).
- **Delete Feed Media**: `DELETE /feed/media/{media_id}`
  - Response: `{"message": "Media item deleted successfully"}`
  - Description: Delete a feed media item (authenticated).
- **Get Feed Media**: `GET /feed/{content_id}/media`
  - Response: `List[FeedMedia]`
  - Description: Retrieve all media for a feed content item.
- **Search Feed**: `GET /feed/search?query={query}`
  - Response: `List[FeedContentWithMedia]`
  - Description: Search feed content by title.

## Professional Endpoints
- **Create Pro Content**: `POST /professionals/{professional_id}/content`
  - Request: `ProContentCreate` (title, description, full_content, preview_content, content_type, price, is_featured)
  - Response: `ProContent`
  - Description: Create professional content (authenticated).
- **Get Pro Content**: `GET /professionals/{professional_id}/content`
  - Response: `List[ProContent]`
  - Description: Retrieve all content for a professional.
- **Create Professional Plan**: `POST /professionals/{professional_id}/plans`
  - Request: `ProfessionalPlanCreate` (plan_type, name, description, price, duration_days, is_active)
  - Response: `ProfessionalPlan`
  - Description: Create a professional plan (authenticated).
- **Get Professional Plans**: `GET /professionals/{professional_id}/plans`
  - Response: `List[ProfessionalPlan]`
  - Description: Retrieve all plans for a professional.
- **Create Group Coaching**: `POST /professionals/{professional_id}/coaching`
  - Request: `GroupCoachingCreate` (title, description, capacity, price)
  - Response: `GroupCoaching`
  - Description: Create a group coaching offering (authenticated).
- **Get Group Coaching**: `GET /professionals/{professional_id}/coaching`
  - Response: `List[GroupCoaching]`
  - Description: Retrieve all group coaching offerings for a professional.
- **Create Mentorship**: `POST /professionals/{professional_id}/mentorship`
  - Request: `MentorshipCreate` (title, description, price)
  - Response: `Mentorship`
  - Description: Create a mentorship offering (authenticated).
- **Get Mentorship**: `GET /professionals/{professional_id}/mentorship`
  - Response: `List[Mentorship]`
  - Description: Retrieve all mentorship offerings for a professional.

## Subscription Endpoints
- **Create Subscription**: `POST /users/{user_id}/subscribe/{plan_id}`
  - Request: `SubscriptionCreate` (payment_method, transaction_id)
  - Response: `Subscription`
  - Description: Subscribe a user to a professional plan (authenticated).
- **Get User Subscriptions**: `GET /users/{user_id}/subscriptions`
  - Response: `List[Subscription]`
  - Description: Retrieve a user's subscriptions (authenticated).

## Admin Endpoints
- **Get Creator Metrics**: `GET /admin/creators/{creator_id}/metrics`
  - Response: `{"creator_id": int, "post_count": int}`
  - Description: Retrieve engagement metrics for a Creator (e.g., number of posts).