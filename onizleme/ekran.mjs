// node ekran.mjs <sunucu-url> <cikti.png> — yerel Webamp önizlemesinden ekran görüntüsü (2x ölçek)
// Gereksinim: playwright-core ve Chrome; PW_ROOT = playwright-core'un kurulu olduğu dizin (varsayılan: geçerli dizin).
import { createRequire } from 'node:module';
const require = createRequire((process.env.PW_ROOT || process.cwd()) + '/');
const { chromium } = require('playwright-core');
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: 700, height: 560 }, deviceScaleFactor: 2 });
const logs = [];
p.on('console', m => logs.push(m.text()));
p.on('pageerror', e => logs.push('HATA ' + e.message));
await p.goto(process.argv[2]);
await p.waitForSelector('#webamp .window', { timeout: 30000 });
await p.waitForTimeout(3500);
await p.screenshot({ path: process.argv[3] });
console.log(await p.evaluate(() => document.querySelectorAll('#webamp .window').length + ' pencere'));
console.log(logs.filter(l => /hata|error/i.test(l)).join('\n') || 'konsol hatası yok');
await b.close();
