<?php
// dom4.php — Image aléatoire avec Tailwind CSS (PHP + Tailwind + JS)
// Sources : Picsum, LoremFlickr, PlaceDog (gratuites, sans clé API) avec bascule automatique.

$largeur = 600;
$hauteur = 400;
?>
<!DOCTYPE html>
<html lang="fr" class="h-full">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DOM4 — Image aléatoire (Tailwind)</title>

<script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="min-h-full bg-slate-100 text-slate-900">

<nav class="bg-blue-600 text-white shadow">
  <div class="mx-auto flex max-w-4xl items-center justify-between px-4 py-4">
    <span class="text-lg font-bold">DOM4 — Image aléatoire</span>
    <span id="source-info" class="rounded-full bg-white px-3 py-1 text-xs font-semibold text-slate-700">
      Chargement…
    </span>
  </div>
</nav>

<main class="mx-auto max-w-4xl px-4 py-8">
  <div class="rounded-2xl bg-white shadow-xl ring-1 ring-slate-900/5 overflow-hidden">

    <div
      id="zone-image"
      class="relative flex min-h-[300px] items-center justify-center overflow-hidden bg-slate-200"
    >
      <img
        id="image-random"
        class="hidden h-full w-full object-cover"
        alt="Image aléatoire"
      >

      <div
        id="spinner"
        class="absolute hidden h-12 w-12 animate-spin rounded-full border-4 border-blue-200 border-t-blue-600"
        role="status"
        aria-label="Chargement"
      ></div>
    </div>

    <div class="p-6 text-center">
      <h1 class="text-xl font-bold sm:text-2xl">
        Découvre une image au hasard
      </h1>

      <p class="mt-2 text-sm text-slate-500">
        Clique sur le bouton ou appuie sur la touche
        <kbd class="rounded border border-slate-300 bg-slate-100 px-1.5 py-0.5 text-xs font-semibold">R</kbd>.
      </p>

      <button
        id="btn-random"
        type="button"
        class="mt-5 inline-flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-6 py-3 text-base font-semibold text-white transition hover:bg-blue-700 focus:outline-none focus-visible:ring-4 focus-visible:ring-blue-300 disabled:cursor-not-allowed disabled:opacity-60"
      >
        <span
          id="btn-spinner"
          class="hidden h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white"
          aria-hidden="true"
        ></span>

        <span id="btn-texte">Charger une autre image</span>
      </button>
    </div>
  </div>

  <div
    id="alerte"
    class="mt-4 hidden rounded-xl px-4 py-3 text-sm font-medium"
    role="alert"
  ></div>
</main>

<script>
  const L = <?= (int)$largeur ?>;
  const H = <?= (int)$hauteur ?>;

  const SOURCES = [
    {
      nom: 'Lorem Picsum',
      url: (r) => `https://picsum.photos/${L}/${H}?random=${r}`
    },
    {
      nom: 'LoremFlickr',
      url: (r) => `https://loremflickr.com/${L}/${H}?random=${r}`
    },
    {
      nom: 'PlaceDog',
      url: (r) => `https://placedog.net/${L}/${H}?random&r=${r}`
    }
  ];

  const img = document.getElementById('image-random');
  const bouton = document.getElementById('btn-random');
  const btnTexte = document.getElementById('btn-texte');
  const btnSpinner = document.getElementById('btn-spinner');
  const spinner = document.getElementById('spinner');
  const alerte = document.getElementById('alerte');
  const infoSrc = document.getElementById('source-info');

  function setAlerte(texte, type) {
    const classes = {
      success: 'bg-green-100 text-green-800 ring-1 ring-green-200',
      danger: 'bg-red-100 text-red-800 ring-1 ring-red-200'
    };

    alerte.textContent = texte;
    alerte.className = 'mt-4 rounded-xl px-4 py-3 text-sm font-medium ' + classes[type];
  }

  function setChargement(actif) {
    bouton.disabled = actif;
    spinner.classList.toggle('hidden', !actif);
    btnSpinner.classList.toggle('hidden', !actif);
    btnTexte.textContent = actif ? 'Chargement...' : 'Charger une autre image';
  }

  function essayerSource(index, resolve, reject) {
    if (index >= SOURCES.length) {
      reject();
      return;
    }

    const source = SOURCES[index];
    const fantome = new Image();
    let termine = false;

    const suivant = () => {
      if (termine) return;
      termine = true;
      clearTimeout(minuteur);
      essayerSource(index + 1, resolve, reject);
    };

    const minuteur = setTimeout(suivant, 6000);

    fantome.onload = () => {
      if (termine) return;
      termine = true;
      clearTimeout(minuteur);
      resolve({
        src: fantome.src,
        nom: source.nom
      });
    };

    fantome.onerror = suivant;

    fantome.src = source.url(
      Date.now() + '' + Math.floor(Math.random() * 1000)
    );
  }

  function chargerImage() {
    setChargement(true);
    alerte.classList.add('hidden');

    new Promise((resolve, reject) => essayerSource(0, resolve, reject))
      .then(({ src, nom }) => {
        img.src = src;
        img.classList.remove('hidden');
        infoSrc.textContent = 'Source : ' + nom;
        setAlerte('✅ Image chargée !', 'success');
      })
      .catch(() => {
        infoSrc.textContent = 'Aucune source';
        setAlerte(
          '❌ Impossible de charger une image. Vérifie ta connexion, un bloqueur de pub ou ton pare-feu.',
          'danger'
        );
      })
      .finally(() => setChargement(false));
  }

  bouton.addEventListener('click', chargerImage);

  document.addEventListener('keydown', (e) => {
    if ((e.key === 'r' || e.key === 'R') && !bouton.disabled) {
      chargerImage();
    }
  });

  chargerImage();
</script>

</body>
</html>