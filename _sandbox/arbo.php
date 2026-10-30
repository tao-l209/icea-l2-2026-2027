<?php
/**
 * _sandbox/arbo.php
 * Génère un fichier texte listant l'arborescence du dossier parent.
 */

// --- Dossier à scanner : le parent de _sandbox ---
$rootDir = realpath(__DIR__ . '/..');

if ($rootDir === false) {
    die("Impossible de résoudre le dossier parent.\n");
}

$outputFile = __DIR__ . '/arbo.txt';

$ignoreNames = [
    '.git', '.idea', '.vscode', 'node_modules', 'vendor',
    'arbo.txt', 'arbo.php',
];

$ignoreExts = ['log', 'tmp', 'cache'];

// --- Fonctions préfixées pour éviter tout conflit ---
function arbo_formatSize(int $bytes): string
{
    $units = ['o', 'Ko', 'Mo', 'Go', 'To'];
    $i = 0;
    while ($bytes >= 1024 && $i < count($units) - 1) {
        $bytes /= 1024;
        $i++;
    }
    return round($bytes, ($i === 0 ? 0 : 1)) . ' ' . $units[$i];
}

function arbo_scanDir(string $dir, string $prefix, array $ignoreNames, array $ignoreExts, int $depth = 0, int $maxDepth = 20): string
{
    if ($depth > $maxDepth) {
        return $prefix . "... (profondeur max atteinte)\n";
    }

    $items = @scandir($dir);
    if ($items === false) {
        return $prefix . "[accès refusé]\n";
    }

    $items = array_filter($items, function ($item) use ($ignoreNames) {
        return $item !== '.' && $item !== '..' && !in_array($item, $ignoreNames, true);
    });
    sort($items, SORT_NATURAL | SORT_FLAG_CASE);

    $count = count($items);
    $i = 0;
    $out = '';

    foreach ($items as $item) {
        $i++;
        $isLast   = ($i === $count);
        $fullPath = $dir . DIRECTORY_SEPARATOR . $item;
        $branch   = $isLast ? '└── ' : '├── ';
        $nextPfx  = $prefix . ($isLast ? '    ' : '│   ');

        if (is_dir($fullPath)) {
            $out .= $prefix . $branch . $item . "/\n";
            $out .= arbo_scanDir($fullPath, $nextPfx, $ignoreNames, $ignoreExts, $depth + 1, $maxDepth);
        } else {
            $ext = strtolower(pathinfo($item, PATHINFO_EXTENSION));
            if (in_array($ext, $ignoreExts, true)) {
                continue;
            }
            $size = @filesize($fullPath);
            $sizeStr = $size !== false ? ' (' . arbo_formatSize($size) . ')' : '';
            $out .= $prefix . $branch . $item . $sizeStr . "\n";
        }
    }

    return $out;
}

// --- Génération ---
$header  = "========================================\n";
$header .= " Arborescence du dossier : $rootDir\n";
$header .= " Généré le : " . date('Y-m-d H:i:s') . "\n";
$header .= "========================================\n\n";
$header .= basename($rootDir) . "/\n";

$tree = arbo_scanDir($rootDir, '', $ignoreNames, $ignoreExts);

if (file_put_contents($outputFile, $header . $tree) === false) {
    die("Impossible d'écrire dans $outputFile\n");
}

echo "✔ Arborescence générée : $outputFile\n";
echo "  Taille : " . arbo_formatSize(filesize($outputFile)) . "\n";