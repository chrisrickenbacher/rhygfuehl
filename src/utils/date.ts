/**
 * Formats an ISO datetime string into a locale-aware format used in the Rhygfuehl app.
 * 
 * @param datetimeStr ISO datetime string (e.g. 2024-03-20T10:00:00Z)
 * @param lang Language code ('de' or 'en')
 * @returns Formatted string (e.g. "Update: 20.03.24, 11:00") or null if invalid
 */
export function formatLocalTime(datetimeStr: string | null, lang: string): string | null {
	if (!datetimeStr || datetimeStr === 'null' || datetimeStr === '') {
		return null;
	}

	try {
		const date = new Date(datetimeStr);
		if (isNaN(date.getTime())) {
			return null;
		}

		// Use de-CH for Swiss German style, en-GB for 24h English style
		return date.toLocaleString(lang === 'de' ? 'de-CH' : 'en-GB', {
			day: '2-digit',
			month: '2-digit',
			year: '2-digit',
			hour: '2-digit',
			minute: '2-digit',
		});
	} catch (e) {
		console.error('Error formatting date:', e);
		return null;
	}
}
