import type { APIRoute } from 'astro';
import waterData from '../../data/data/waterData.json';
import airData from '../../data/data/airData.json';
import levelData from '../../data/data/levelData.json';
import qualityData from '../../data/data/qualityData.json';
import de from '../locales/de.json';

const getPrognosisLabel = (q: number, t: any) => {
	if (q === 3) return t.prognosisExcellent;
	if (q === 2) return t.prognosisGood;
	return t.prognosisDiscouraged;
};

const getQualityLabel = (q: number, t: any) => {
	if (q === 3) return t.qualityExcellent;
	if (q === 2) return t.qualityGood;
	return t.qualityDiscouraged;
};

const getSafetyLabel = (s: number, t: any) => {
	if (s === 3) return t.safetySafe;
	if (s === 2) return t.safetyCaution;
	return t.safetyDiscouraged;
};

export const GET: APIRoute = async () => {
	const waterTemp = waterData.actualValue.toFixed(1);
	const airTemp = airData.actualValue.toFixed(1);
	const waterLevel = levelData.actualValue > 0 ? `+${levelData.actualValue.toFixed(2)}` : levelData.actualValue.toFixed(2);

	const prognosisLabel = getPrognosisLabel(qualityData.quality, de);
	const qualityLabel = getQualityLabel(qualityData.indices?.quality, de);
	const safetyLabel = getSafetyLabel(qualityData.indices?.safety, de);

	const content = `# rhygfuehl.ch

> rhygfuehl.ch shows the current Rhine temperature of Basel in a clear app that can be easily accessed via a web browser. The app also shows a simplified temperature history of the last 12 hours and the current air temperature at Untere Rheingasse.

Current data for the Rhine in Basel:
- Water temperature: ${waterTemp} °C
- Air temperature: ${airTemp} °C
- Water level: ${waterLevel} m
- Swimming prognosis: ${prognosisLabel} (Water Quality: ${qualityLabel}, Safety: ${safetyLabel})
- Last Update: ${waterData.lastUpdate}

## Swimming Prognosis Logic

The swimming recommendation is calculated by assessing two independent indices:
- **Water Quality** (microbiological risk): Focuses on bacterial risk from rain (sewer overflows) and lack of natural disinfection (global radiation).
- **Swimmer Safety** (physical risk): Focuses on immediate physical dangers, primarily cold shock (water temperature).

## Links

- [Project on GitHub](https://github.com/chrisrickenbacher/rhygfuehl): The source code for rhygfuehl.ch.
- [Prognosis Logic](https://github.com/chrisrickenbacher/rhygfuehl/blob/master/docs/prognosis-logic.md): Detailed documentation on how the swimming prognosis is calculated.
`;

	return new Response(content, {
		headers: {
			'Content-Type': 'text/plain; charset=utf-8',
		},
	});
};
