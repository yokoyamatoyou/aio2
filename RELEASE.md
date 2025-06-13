# Release Procedure

1. **Build** the final application package if needed.
2. **Verify environment variables** such as `OPENAI_API_KEY` are set in the target deployment environment.
3. **Run unit tests** using `python -m unittest discover tests` and ensure all tests pass.
4. **Deploy** the application to the production server with `streamlit run seo_aio_streamlit.py` or your container setup.
5. **Monitor logs** for any unexpected errors.

## Rollback

If issues occur after deployment:
1. Stop the running service.
2. Revert to the previous stable commit in version control.
3. Redeploy using the prior build artifacts or commit.
