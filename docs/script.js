
// ===== TRANSLATIONS =====
const translations = {
  pt: {
    pageTitle: 'Códigos de Cidades QWeather para Relógios ESP8266',
    navSearch: 'Busca',
    navInstructions: 'Instruções',
    darkModeTitle: 'Alternar modo escuro',
    langToggleTitle: 'Switch to English',
    heroTitle: 'Códigos de Cidades QWeather',
    heroLead: 'Encontre os códigos de cidade do site QWeather para configurar a previsão do tempo em relógios chineses construídos com ESP8266.',
    heroSearchBtn: '<i class="fas fa-search me-2"></i> Buscar Cidade',
    heroHowToBtn: '<i class="fas fa-info-circle me-2"></i> Como Usar',
    searchTitle: 'Buscar Código de Cidade',
    searchDesc: 'Digite o nome da cidade para encontrar seu código do site QWeather. Você pode incluir o estado para resultados mais precisos (ex: "São Paulo, SP").',
    searchPlaceholder: 'Nome da cidade (ex: Rio de Janeiro, RJ)',
    searchBtn: '<i class="fas fa-search"></i> Buscar',
    loadingText: 'Carregando dados...',
    resultsHeader: 'Resultados da Busca',
    thCode: 'Código',
    thCity: 'Cidade',
    thState: 'Estado',
    thActions: 'Ações',
    noResults: 'Nenhuma cidade encontrada com esse nome. Tente outro termo ou verifique a ortografia.',
    instrTitle: 'Como Usar o Código da Cidade',
    step1Title: '1. Encontre o Código',
    step1Text: 'Use a ferramenta de busca acima para encontrar o código da sua cidade.',
    step2Title: '2. Copie o Código',
    step2Text: 'Clique no botão de cópia ao lado do código da cidade desejada.',
    step3Title: '3. Configure seu Relógio',
    step3Text: 'Abra as configurações do seu relógio e cole o código na configuração de previsão do tempo.',
    configHeader: 'Exemplo de Configuração',
    configDesc: 'A maioria dos relógios chineses com previsão do tempo usa a API QWeather. Para configurar a previsão do tempo, você precisará inserir o código da cidade no aplicativo do relógio.',
    configStepsLabel: 'Passos típicos:',
    configStep1: 'Abra o hotspot do seu relógio, irá aparecer o IP na tela.',
    configStep2: 'Vá para as configurações do relógio',
    configStep3: 'Encontre a opção de previsão do tempo ou clima',
    configStep4: 'Insira o código da cidade que você encontrou neste site',
    configStep5: 'Salve as configurações e sincronize seu relógio',
    faqTitle: 'Perguntas Frequentes',
    faq1Q: 'O que é um código QWeather?',
    faq1A: 'QWeather é um serviço de previsão do tempo usado por muitos relógios inteligentes chineses. Cada cidade tem um código único que o relógio usa para buscar a previsão do tempo para aquela localidade.',
    faq2Q: 'Por que preciso deste código?',
    faq2A: 'Muitos relógios inteligentes chineses não conseguem detectar automaticamente sua localização ou não têm uma interface para buscar cidades pelo nome. Em vez disso, eles exigem que você insira manualmente o código da cidade para configurar a previsão do tempo.',
    faq3Q: 'Não encontrei minha cidade. O que fazer?',
    faq3A: 'Se sua cidade não estiver na lista, tente buscar por uma cidade maior próxima. Cidades pequenas podem não estar disponíveis na API QWeather. Alternativamente, você pode tentar buscar pelo nome da região ou município.',
    faq4Q: 'A previsão do tempo não está funcionando no meu relógio. O que fazer?',
    faq4A: 'Verifique se você inseriu o código correto. Alguns relógios podem exigir um formato específico ou ter limitações. Certifique-se também de que seu relógio está conectado ao Wi-Fi e que o aplicativo tem permissão para acessar a internet. Se o problema persistir, tente reiniciar o relógio e as configurações segurando o botão de reset por alguns segundos.',
    footerDesc: 'Uma ferramenta para encontrar códigos de cidade QWeather para relógios com previsão do tempo.',
    footerLinksTitle: 'Links',
    footerResourcesTitle: 'Recursos',
    footerReportIssue: 'Reportar Problema',
    footerLicense: 'Licenciado sob <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a> — Luan Dias, 2023–<span id="currentYear">' + new Date().getFullYear() + '</span>. Código disponível no <a href="https://github.com/luandiasrj/qweather-city-codes" target="_blank">GitHub</a>.',
    // Dynamic JS strings
    toastCopySuccess: 'Código {code} copiado para a área de transferência!',
    toastCopyError: 'Erro ao copiar código. Tente novamente.',
    toastLoadError: 'Erro ao carregar dados. Tente novamente mais tarde.',
    toastSearchEmpty: 'Digite o nome de uma cidade para buscar.',
    copyBtnTitle: 'Copiar código',
    osmBtnTitle: 'Abrir no OpenStreetMap',
    geoBtnTitle: 'Abrir no aplicativo de mapas do dispositivo'
  },
  en: {
    pageTitle: 'QWeather City Codes for ESP8266 Clocks',
    navSearch: 'Search',
    navInstructions: 'Instructions',
    darkModeTitle: 'Toggle dark mode',
    langToggleTitle: 'Mudar para Português',
    heroTitle: 'QWeather City Codes',
    heroLead: 'Find QWeather city codes to configure weather forecasts on Chinese clocks built with ESP8266.',
    heroSearchBtn: '<i class="fas fa-search me-2"></i> Search City',
    heroHowToBtn: '<i class="fas fa-info-circle me-2"></i> How to Use',
    searchTitle: 'Search City Code',
    searchDesc: 'Enter the city name to find its QWeather code. You can include the state for more precise results (e.g., "São Paulo, SP").',
    searchPlaceholder: 'City name (e.g., Rio de Janeiro, RJ)',
    searchBtn: '<i class="fas fa-search"></i> Search',
    loadingText: 'Loading data...',
    resultsHeader: 'Search Results',
    thCode: 'Code',
    thCity: 'City',
    thState: 'State',
    thActions: 'Actions',
    noResults: 'No city found with that name. Try another term or check the spelling.',
    instrTitle: 'How to Use the City Code',
    step1Title: '1. Find the Code',
    step1Text: 'Use the search tool above to find your city code.',
    step2Title: '2. Copy the Code',
    step2Text: 'Click the copy button next to the desired city code.',
    step3Title: '3. Set Up Your Clock',
    step3Text: 'Open your clock settings and paste the code in the weather forecast configuration.',
    configHeader: 'Configuration Example',
    configDesc: 'Most Chinese clocks with weather forecast use the QWeather API. To configure the weather forecast, you will need to enter the city code in the clock application.',
    configStepsLabel: 'Typical steps:',
    configStep1: 'Open the hotspot on your clock, the IP will appear on the screen.',
    configStep2: 'Go to the clock settings',
    configStep3: 'Find the weather or climate forecast option',
    configStep4: 'Enter the city code you found on this site',
    configStep5: 'Save the settings and sync your clock',
    faqTitle: 'Frequently Asked Questions',
    faq1Q: 'What is a QWeather code?',
    faq1A: 'QWeather is a weather forecast service used by many Chinese smart clocks. Each city has a unique code that the clock uses to fetch the weather forecast for that location.',
    faq2Q: 'Why do I need this code?',
    faq2A: 'Many Chinese smart clocks cannot automatically detect your location or do not have an interface to search cities by name. Instead, they require you to manually enter the city code to configure the weather forecast.',
    faq3Q: "I can't find my city. What should I do?",
    faq3A: 'If your city is not on the list, try searching for a larger nearby city. Small cities may not be available in the QWeather API. Alternatively, you can try searching by region or municipality name.',
    faq4Q: 'The weather forecast is not working on my clock. What should I do?',
    faq4A: 'Make sure you entered the correct code. Some clocks may require a specific format or have limitations. Also make sure your clock is connected to Wi-Fi and that the app has permission to access the internet. If the problem persists, try restarting the clock and settings by holding the reset button for a few seconds.',
    footerDesc: 'A tool to find QWeather city codes for weather forecast clocks.',
    footerLinksTitle: 'Links',
    footerResourcesTitle: 'Resources',
    footerReportIssue: 'Report Issue',
    footerLicense: 'Licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a> — Luan Dias, 2023–<span id="currentYear">' + new Date().getFullYear() + '</span>. Source code available on <a href="https://github.com/luandiasrj/qweather-city-codes" target="_blank">GitHub</a>.',
    // Dynamic JS strings
    toastCopySuccess: 'Code {code} copied to clipboard!',
    toastCopyError: 'Error copying code. Please try again.',
    toastLoadError: 'Error loading data. Please try again later.',
    toastSearchEmpty: 'Enter a city name to search.',
    copyBtnTitle: 'Copy code',
    osmBtnTitle: 'Open in OpenStreetMap',
    geoBtnTitle: 'Open in device map app'
  }
};

// ===== i18n SYSTEM =====
let currentLang = 'pt';

function detectLanguage() {
  const saved = localStorage.getItem('lang');
  if (saved && (saved === 'pt' || saved === 'en')) return saved;
  const nav = (navigator.language || navigator.userLanguage || 'pt').toLowerCase();
  return nav.startsWith('pt') ? 'pt' : 'en';
}

function t(key) {
  return (translations[currentLang] && translations[currentLang][key]) || key;
}

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('lang', lang);

  // Update html lang attribute
  document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';

  // Update all elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang][key] !== undefined) {
      el.innerHTML = translations[lang][key];
    }
  });

  // Update placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (translations[lang][key] !== undefined) {
      el.placeholder = translations[lang][key];
    }
  });

  // Update titles
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    const key = el.getAttribute('data-i18n-title');
    if (translations[lang][key] !== undefined) {
      el.title = translations[lang][key];
    }
  });

  // Update language toggle button
  const langBtn = document.getElementById('langToggle');
  if (langBtn) {
    // Show current language flag
    langBtn.innerHTML = lang === 'pt' ? '<span class="fi fi-br"></span>' : '<span class="fi fi-us"></span>';
  }
}

function toggleLanguage() {
  const newLang = currentLang === 'pt' ? 'en' : 'pt';
  applyLanguage(newLang);
}

// ===== DOM ELEMENTS =====
const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const resultsTable = document.getElementById('resultsTable');
const resultsContainer = document.getElementById('resultsContainer');
const noResults = document.getElementById('noResults');
const loadingIndicator = document.getElementById('loadingIndicator');
const darkModeToggle = document.getElementById('darkModeToggle');
const langToggle = document.getElementById('langToggle');
const body = document.body;

// ===== DEBOUNCE =====
function debounce(func, wait) {
  let timeout;
  return function (...args) {
    const context = this;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), wait);
  };
}

// ===== DARK MODE =====
function setDarkMode(isDark) {
  if (isDark) {
    body.classList.add('dark-mode');
  } else {
    body.classList.remove('dark-mode');
  }
  updateDarkModeIcon(isDark);
}

function toggleDarkMode() {
  const isDark = !body.classList.contains('dark-mode');
  setDarkMode(isDark);
  localStorage.setItem('darkMode', isDark ? 'true' : 'false');
}

function updateDarkModeIcon(isDarkMode) {
  const icon = darkModeToggle.querySelector('i');
  if (isDarkMode) {
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
  } else {
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
  }
}

// Initialize dark mode: saved preference > system preference
function initDarkMode() {
  const saved = localStorage.getItem('darkMode');
  if (saved !== null) {
    setDarkMode(saved === 'true');
  } else {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setDarkMode(prefersDark);
  }

  // Listen for system theme changes (only when no manual override)
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (localStorage.getItem('darkMode') === null) {
      setDarkMode(e.matches);
    }
  });
}

initDarkMode();

if (darkModeToggle) {
  darkModeToggle.addEventListener('click', () => {
    toggleDarkMode();
  });
}

if (langToggle) {
  langToggle.addEventListener('click', () => {
    toggleLanguage();
  });
}

// Initialize language
const detectedLang = detectLanguage();
applyLanguage(detectedLang);

// Update year
const yearSpans = document.querySelectorAll('#currentYear');
yearSpans.forEach(span => { span.textContent = new Date().getFullYear(); });

// ===== CITY DATA =====
let cityData = [];

async function loadCityData() {
  try {
    showLoading(true);

    const response = await fetch('./Brasil-City-List-latest.csv');
    const csvText = await response.text();

    const lines = csvText.split('\n');
    const headers = lines[0].split(',');

    const cities = [];

    for (let i = 1; i < lines.length; i++) {
      if (!lines[i].trim()) continue;

      const values = lines[i].split(',');
      if (values.length < 9) continue;

      const city = {
        id: values[0],
        name: values[1],
        country: values[3],
        state: values[4],
        adm2: values[5],
        timezone: values[6],
        latitude: values[7],
        longitude: values[8]
      };

      cities.push(city);
    }

    cityData = cities;
    console.log(`Data loaded: ${cityData.length} cities`);

    return cities;
  } catch (error) {
    console.error('Error loading data:', error);
    showToast(t('toastLoadError'), 'error');
    return [];
  } finally {
    showLoading(false);
  }
}

function normalizeText(text) {
  return text.toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function searchCities(query) {
  if (!query || query.length < 2) return [];

  const normalizedQuery = normalizeText(query);
  let parts = normalizedQuery.split(',');
  const cityQuery = parts[0].trim();
  const stateQuery = parts.length > 1 ? parts[1].trim() : '';

  return cityData.filter(city => {
    const cityName = normalizeText(city.name);
    const stateName = normalizeText(city.state);
    const adm2Name = normalizeText(city.adm2);

    if (stateQuery) {
      return (cityName.includes(cityQuery) || adm2Name.includes(cityQuery)) &&
        stateName.includes(stateQuery);
    }

    return cityName.includes(cityQuery) || adm2Name.includes(cityQuery);
  });
}

function displayResults(results) {
  resultsTable.innerHTML = '';

  if (results.length === 0) {
    resultsContainer.classList.add('d-none');
    noResults.classList.remove('d-none');
    return;
  }

  noResults.classList.add('d-none');
  resultsContainer.classList.remove('d-none');

  results.forEach(city => {
    const row = document.createElement('tr');

    // Code cell with copy button
    const codeCell = document.createElement('td');
    const codeContainer = document.createElement('div');
    codeContainer.className = 'd-flex align-items-center';

    const codeSpan = document.createElement('span');
    codeSpan.className = 'city-code me-2';
    codeSpan.textContent = city.id;

    const copyButton = document.createElement('button');
    copyButton.className = 'btn btn-sm btn-outline-primary copy-btn';
    copyButton.innerHTML = '<i class="fas fa-copy"></i>';
    copyButton.title = t('copyBtnTitle');
    copyButton.addEventListener('click', () => {
      navigator.clipboard.writeText(city.id)
        .then(() => {
          showToast(t('toastCopySuccess').replace('{code}', city.id), 'success');
        })
        .catch(err => {
          console.error('Copy error:', err);
          showToast(t('toastCopyError'), 'error');
        });
    });

    codeContainer.appendChild(codeSpan);
    codeContainer.appendChild(copyButton);
    codeCell.appendChild(codeContainer);

    // City
    const cityCell = document.createElement('td');
    cityCell.textContent = city.name;

    // State
    const stateCell = document.createElement('td');
    stateCell.textContent = city.state;

    // Actions - Map buttons
    const actionsCell = document.createElement('td');

    const osmButton = document.createElement('a');
    osmButton.className = 'btn btn-sm btn-outline-info me-1 desktop-only';
    osmButton.href = `https://www.openstreetmap.org/?mlat=${city.latitude}&mlon=${city.longitude}&zoom=14`;
    osmButton.target = '_blank';
    osmButton.innerHTML = '<i class="fas fa-map-marker-alt"></i> OSM';
    osmButton.title = t('osmBtnTitle');
    actionsCell.appendChild(osmButton);

    const geoButton = document.createElement('a');
    geoButton.className = 'btn btn-sm btn-outline-success mobile-only';
    geoButton.href = `geo:${city.latitude},${city.longitude}`;
    geoButton.innerHTML = '<i class="fas fa-mobile-alt"></i> App';
    geoButton.title = t('geoBtnTitle');
    actionsCell.appendChild(geoButton);

    if (!window.matchMedia('(max-width: 768px)').matches) {
      geoButton.style.display = 'none';
    }

    row.appendChild(codeCell);
    row.appendChild(cityCell);
    row.appendChild(stateCell);
    row.appendChild(actionsCell);

    resultsTable.appendChild(row);
  });
}

function showLoading(show) {
  if (show) {
    loadingIndicator.classList.remove('d-none');
    resultsContainer.classList.add('d-none');
    noResults.classList.add('d-none');
  } else {
    loadingIndicator.classList.add('d-none');
  }
}

function showToast(message, type = 'info') {
  const toastContainer = document.querySelector('.toast-container');

  const toast = document.createElement('div');
  toast.className = `toast show toast-${type}`;
  toast.setAttribute('role', 'alert');
  toast.setAttribute('aria-live', 'assertive');
  toast.setAttribute('aria-atomic', 'true');

  const toastBody = document.createElement('div');
  toastBody.className = 'toast-body d-flex';

  let icon = 'info-circle';
  if (type === 'success') icon = 'check-circle';
  if (type === 'error') icon = 'exclamation-circle';

  toastBody.innerHTML = `
        <div class="me-2">
          <i class="fas fa-${icon}"></i>
        </div>
        <div>
          ${message}
        </div>
        <div class="ms-auto">
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
      `;

  toast.appendChild(toastBody);
  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => {
      toastContainer.removeChild(toast);
    }, 500);
  }, 5000);
}

// ===== EVENT LISTENERS =====

searchInput.addEventListener('input', debounce(async (e) => {
  const query = e.target.value.trim();

  if (query.length >= 2) {
    if (cityData.length === 0) {
      await loadCityData();
    }
    const results = searchCities(query);
    displayResults(results);
  } else {
    resultsContainer.classList.add('d-none');
    noResults.classList.add('d-none');
  }
}, 300));

searchButton.addEventListener('click', async () => {
  const query = searchInput.value.trim();

  if (!query) {
    showToast(t('toastSearchEmpty'), 'error');
    return;
  }

  if (cityData.length === 0) {
    await loadCityData();
  }

  const results = searchCities(query);
  displayResults(results);
});

searchInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    searchButton.click();
  }
});

document.addEventListener('DOMContentLoaded', async () => {
  await loadCityData();
});
