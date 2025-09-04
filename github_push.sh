#!/bin/bash

# GitHub Push Script for Fractal-Harmonic Transform Paper
# Usage: ./github_push.sh YOUR_GITHUB_USERNAME

if [ $# -eq 0 ]; then
    echo "❌ Error: Please provide your GitHub username"
    echo "Usage: ./github_push.sh YOUR_USERNAME"
    echo "Example: ./github_push.sh johnsmith"
    exit 1
fi

USERNAME=$1
REPO_URL="https://github.com/$USERNAME/fractal-harmonic-transform.git"

echo "🚀 Setting up GitHub repository for Fractal-Harmonic Transform"
echo "   Username: $USERNAME"
echo "   Repository: fractal-harmonic-transform"
echo ""

# Check if remote already exists
if git remote get-url origin >/dev/null 2>&1; then
    echo "⚠️  GitHub remote already exists. Updating..."
    git remote set-url origin "$REPO_URL"
else
    echo "📡 Adding GitHub remote..."
    git remote add origin "$REPO_URL"
fi

echo "⬆️  Pushing to GitHub..."
if git push -u origin main; then
    echo ""
    echo "✅ SUCCESS! Repository pushed to GitHub"
    echo ""
    echo "🌐 Your repository is now live at:"
    echo "   https://github.com/$USERNAME/fractal-harmonic-transform"
    echo ""
    echo "🎯 Next steps:"
    echo "   1. Go to your GitHub repository"
    echo "   2. Add repository topics (mathematics, physics, etc.)"
    echo "   3. Add repository description"
    echo "   4. Share the link on social media and academic networks"
    echo ""
    echo "📊 Repository Contents:"
    echo "   📄 Complete research paper (LaTeX)"
    echo "   📊 Validation results and statistical analysis"
    echo "   📚 Mathematical framework documentation"
    echo "   🚀 arXiv submission package"
    echo "   🛠️  Deployment and setup guides"
    echo ""
    echo "🎉 Your groundbreaking research is now publicly available!"
else
    echo ""
    echo "❌ Push failed. This might be because:"
    echo "   1. The GitHub repository doesn't exist yet"
    echo "   2. You don't have permission to push to the repository"
    echo "   3. There's an authentication issue"
    echo ""
    echo "🔧 Troubleshooting:"
    echo "   1. Make sure you created the repository on GitHub first"
    echo "   2. Verify your GitHub username is correct"
    echo "   3. Check if you need to set up SSH keys or personal access tokens"
    echo ""
    echo "📞 For help, visit: https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories"
fi