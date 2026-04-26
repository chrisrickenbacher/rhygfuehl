import { describe, it, expect } from 'vitest';
import { formatLocalTime } from '../../src/utils/date';

describe('formatLocalTime', () => {
	const mockDate = '2024-04-26T15:30:00Z';

	it('formats a date string for German (de-CH style)', () => {
		const result = formatLocalTime(mockDate, 'de');
		// toLocaleString output can vary slightly by environment (especially time zones)
		expect(result).toMatch(/26\.04\.24/);
		// Check that it contains a time format like HH:MM
		expect(result).toMatch(/\d{2}:\d{2}/);
	});

	it('formats a date string for English (en-GB style)', () => {
		const result = formatLocalTime(mockDate, 'en');
		expect(result).toMatch(/26\/04\/24/);
		expect(result).toMatch(/\d{2}:\d{2}/);
	});

	it('returns null for empty input', () => {
		expect(formatLocalTime('', 'de')).toBeNull();
		expect(formatLocalTime(null, 'de')).toBeNull();
		expect(formatLocalTime('null', 'de')).toBeNull();
	});

	it('returns null for invalid date strings', () => {
		expect(formatLocalTime('invalid-date', 'de')).toBeNull();
	});
});
