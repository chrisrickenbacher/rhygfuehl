<div align="center">

# rhygfuehl.ch



☀️ rhygfuehl.ch shows the current Rhine temperature of Basel in a clear app that can be easily accessed via a web browser. The app also shows a simplified temperature history of the last 12 hours and the current air temperature at Untere Rheingasse.

<h3>Support this project:</h3>
<p><a href="https://www.buymeacoffee.com/rhygfuehl" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;" ></a></p>

</div>

## How it works

The application uses **Astro** for pre-rendering a static site with extreme SEO optimization and zero baseline JavaScript. 

Every 15 minutes, a GitHub Actions cron job triggers the `data/aggregation.py` script to fetch the latest Rhine temperatures and water levels from the Open Data Basel-Stadt APIs. The script writes this data into static JSON files. 

Immediately after fetching, the GitHub Action builds the Astro site, directly injecting the latest temperatures into the HTML `<meta name="description">` tags for immediate SEO indexing, and then deploys to GitHub Pages.

## Local Development

To run this project locally, ensure you have Node.js installed.

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the local development server:**
   ```bash
   npm run dev
   ```
   The site will be available at `http://localhost:4321`.

3. **Build for production:**
   ```bash
   npm run build
   ```
   The static output will be generated in the `dist/` directory.

## Testing

This project has a comprehensive testing suite covering frontend components, end-to-end user flows, and backend logic.

### Running Tests Locally

1. **Frontend Unit Tests (Vitest):**
   ```bash
   npm run test:unit
   ```

2. **E2E Tests (Playwright):**
   ```bash
   npx playwright install # First time only
   npm run test:e2e
   ```

3. **Backend Tests (pytest):**
   ```bash
   pip install -r data/requirements.txt
   PYTHONPATH=./data pytest tests/backend/
   ```

### CI/CD

Tests are automatically executed on every Pull Request to `master` and must pass before any manual code change is deployed. Scheduled data updates skip UI testing to ensure high frequency and reliability.

## Contributing

Contributions, issues and feature requests are welcome!
Feel free to check [the issues page](https://github.com/chrisrickenbacher/rhygfuehl/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
