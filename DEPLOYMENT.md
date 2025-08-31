# Django Movie Review API - Deployment Guide

## Free Hosting Options for Learning

### Option 1: Railway (Recommended)
Railway offers $5 free credit monthly and is very beginner-friendly.

#### Steps to Deploy on Railway:

1. **Prepare Your Project**
   - All files are already configured in your project
   - Make sure all changes are committed to Git

2. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub (recommended)

3. **Deploy Your Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your GitHub account and select your repository
   - Railway will auto-detect it's a Django project

4. **Add Environment Variables**
   In Railway dashboard, go to Variables tab and add:
   ```
   SECRET_KEY=secret-key
   DEBUG=False
   DJANGO_SETTINGS_MODULE=movie_review.settings
   ```
   
   **Note**: This is a generated secret key for your project. Keep it secure!
   **Important**: Remove PYTHONPATH=/app as it can cause import issues on Railway.

5. **Deploy**
   - Railway will automatically build and deploy your app
   - You'll get a URL like: `https://your-app-name.railway.app`

### Option 2: Render.com
Render offers free tier with some limitations but is great for learning.

#### Steps for Render:

1. **Create Account** at [render.com](https://render.com)
2. **Create New Web Service**
3. **Connect GitHub Repository**
4. **Configure Settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn movie_review.wsgi:application`
   - Environment Variables:
     ```
     SECRET_KEY=48b+zadw4=!&63&giw+kcw_xmt0yq6&cs(z)xc!#hwg6k@&d3&
     DEBUG=False
     PYTHON_VERSION=3.11.0
     ```

### Option 3: PythonAnywhere (Free Tier)
Good for learning but has some limitations.

1. **Create Account** at [pythonanywhere.com](https://pythonanywhere.com)
2. **Upload Your Code** via Git or Files
3. **Create Web App** with Django framework
4. **Configure WSGI** file to point to your project

## Important Notes for Production:

1. **Database**: For production, consider using PostgreSQL instead of SQLite
2. **Static Files**: WhiteNoise is configured to serve static files
3. **Security**: The current settings are configured for learning/demo purposes
4. **Environment Variables**: Never commit sensitive data like SECRET_KEY to Git

## Testing Your Deployment:

After deployment, test these endpoints:
- `GET /` - Should show your API documentation (drf-yasg)
- `GET /api/` - Your API endpoints
- `POST /api/auth/` - Authentication endpoints

## Local Development:

To run locally with production-like settings:
1. Create a `.env` file (copy from `.env.example`)
2. Set `DEBUG=True` in your `.env` file
3. Run: `python manage.py runserver`

## Troubleshooting:

### Common Railway Deployment Issues:

1. **Import Module Error**: 
   - Make sure DJANGO_SETTINGS_MODULE=movie_review.settings is set in environment variables
   - Remove PYTHONPATH=/app if present

2. **Static Files Not Loading**: Check STATIC_ROOT and WhiteNoise configuration

3. **Database Errors**: 
   - Ensure migrations are run: `python manage.py migrate`
   - Check if DATABASE_URL is properly set for PostgreSQL

4. **Import Errors**: Check all dependencies are in requirements.txt

5. **Worker Process Crashes**:
   - Check Railway logs for specific error messages
   - Ensure Procfile is correctly configured
   - Verify SECRET_KEY is set in environment variables

### Railway-Specific Tips:
- Railway automatically runs `pip install -r requirements.txt`
- The PORT environment variable is automatically set by Railway
- Use Railway's PostgreSQL add-on for production database
- Check the "Deploy" tab in Railway dashboard for real-time logs

## Next Steps for Learning:

1. Add custom domain (available on most platforms)
2. Set up CI/CD pipeline
3. Add monitoring and logging
4. Implement proper database backup
5. Add caching (Redis)
6. Set up proper production database (PostgreSQL)
