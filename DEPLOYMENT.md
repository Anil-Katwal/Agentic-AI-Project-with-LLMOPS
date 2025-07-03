# Deployment Guide for AI Trip Planner on Render

This guide will help you deploy your AI Trip Planner application to Render using Docker.

## Prerequisites

1. A Render account (free tier available)
2. Your code pushed to a Git repository (GitHub, GitLab, etc.)
3. Your Groq API key

## Step 1: Prepare Your Repository

Make sure your repository contains:
- `Dockerfile`
- `requirements.txt`
- `main.py`
- All your application code
- `.dockerignore` (optional but recommended)

## Step 2: Deploy to Render

### Option A: Using Render Dashboard

1. **Sign in to Render**
   - Go to [render.com](https://render.com)
   - Sign in or create an account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your Git repository
   - Select the repository containing your AI Trip Planner

3. **Configure the Service**
   - **Name**: `ai-trip-planner` (or your preferred name)
   - **Environment**: `Docker`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (if code is in root)
   - **Build Command**: `docker build -t ai-trip-planner .`
   - **Start Command**: `docker run -p $PORT:8000 ai-trip-planner`

4. **Set Environment Variables**
   - Click "Environment" tab
   - Add your API keys:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Optionally add other API keys if you have them:
     ```
     OPENAI_API_KEY=your_openai_api_key
     OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
     EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy your application

### Option B: Using render.yaml (Infrastructure as Code)

1. **Push your code** with the `render.yaml` file to your repository

2. **Create Blueprint Instance**
   - Go to Render Dashboard
   - Click "New +" → "Blueprint"
   - Connect your repository
   - Render will automatically detect and use the `render.yaml` configuration

3. **Set Environment Variables**
   - Go to your service settings
   - Add your API keys in the Environment tab

## Step 3: Verify Deployment

1. **Check Health Endpoint**
   - Visit: `https://your-app-name.onrender.com/health`
   - Should return: `{"status": "healthy", "message": "AI Trip Planner is running"}`

2. **Test API Endpoint**
   - Visit: `https://your-app-name.onrender.com/`
   - Should show API information

3. **Test Query Endpoint**
   ```bash
   curl -X POST "https://your-app-name.onrender.com/query" \
        -H "Content-Type: application/json" \
        -d '{"question": "Plan a trip to Paris for 3 days"}'
   ```

## Step 4: Environment Variables

Make sure to set these environment variables in Render:

### Required
- `GROQ_API_KEY`: Your Groq API key

### Optional (for enhanced features)
- `OPENAI_API_KEY`: OpenAI API key (alternative to Groq)
- `OPENWEATHERMAP_API_KEY`: For weather information
- `EXCHANGE_RATE_API_KEY`: For currency conversion
- `GPLACES_API_KEY`: For Google Places search
- `TAVILY_API_KEY`: For Tavily search

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check that all dependencies are in `requirements.txt`
   - Verify Dockerfile syntax
   - Check build logs in Render dashboard

2. **Application Crashes**
   - Check application logs in Render dashboard
   - Verify environment variables are set correctly
   - Ensure API keys are valid

3. **Health Check Fails**
   - Verify the `/health` endpoint is working
   - Check if the application is starting correctly

### Logs and Monitoring

- **View Logs**: Go to your service → "Logs" tab
- **Monitor**: Use the "Metrics" tab to monitor performance
- **Debug**: Use "Shell" tab for debugging if needed

## Cost Optimization

- **Free Tier**: Render offers a free tier with limitations
- **Auto-sleep**: Free services sleep after 15 minutes of inactivity
- **Upgrade**: Consider paid plans for production use

## Security Notes

- Never commit API keys to your repository
- Use environment variables for all sensitive data
- Consider using Render's secret management for production

## Next Steps

1. **Custom Domain**: Add a custom domain in Render settings
2. **SSL**: Render provides automatic SSL certificates
3. **Monitoring**: Set up alerts and monitoring
4. **CI/CD**: Connect to GitHub for automatic deployments

## Support

- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)
- [Docker Documentation](https://docs.docker.com/) 