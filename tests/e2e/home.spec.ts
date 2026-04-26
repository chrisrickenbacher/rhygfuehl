import { test, expect } from '@playwright/test';

test.describe('Home Page', () => {

  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('has correct title and basic metrics (German)', async ({ page }) => {
    await expect(page).toHaveTitle(/Rhygfuehl/i);

    const waterTempHeader = page.getByRole('heading', { name: /Wassertemperatur/i });
    await expect(waterTempHeader.first()).toBeVisible();

    const airTempHeader = page.getByRole('heading', { name: /Lufttemperatur/i });
    await expect(airTempHeader.first()).toBeVisible();

    const prognosisHeader = page.getByRole('heading', { name: /Schwimm-Prognose/i });
    await expect(prognosisHeader.first()).toBeVisible();
  });

  test('can expand and collapse metric details', async ({ page }) => {
    const firstToggle = page.locator('.metric-toggle').first();
    const collapseGrid = page.locator('.collapse-grid').first();

    // Ensure it's closed initially
    await expect(collapseGrid).not.toHaveClass(/is-open/);

    // Click to open
    await firstToggle.click();
    await expect(collapseGrid).toHaveClass(/is-open/);

    // Click again to close
    await firstToggle.click();
    await expect(collapseGrid).not.toHaveClass(/is-open/);
  });

  test('can switch to English translation', async ({ page }) => {
    // Look for link with exact href or text
    const enLink = page.locator('footer a[href="/en/"], nav a[href="/en/"], a[href="/en/"]').first();
    
    if (await enLink.isVisible()) {
      await enLink.click();
      await expect(page).toHaveURL(/\/en\//);

      const waterTempHeaderEn = page.getByRole('heading', { name: /Water temperature/i });
      await expect(waterTempHeaderEn.first()).toBeVisible();

      const prognosisHeaderEn = page.getByRole('heading', { name: /Swimming Prognosis/i });
      await expect(prognosisHeaderEn.first()).toBeVisible();
    }
  });

  test('can navigate to Impressum', async ({ page }) => {
    const impressumLink = page.getByRole('link', { name: /Impressum/i }).first();
    await impressumLink.click();

    await expect(page).toHaveURL(/\/impressum/);
    const impressumHeading = page.getByRole('heading', { name: /Impressum/i }).first();
    await expect(impressumHeading).toBeVisible();

    const backLink = page.getByRole('link', { name: /Zurück/i }).first();
    await backLink.click();
    await expect(page).toHaveURL(/\//);
  });
});
