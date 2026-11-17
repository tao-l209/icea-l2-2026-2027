<?php
// ultra_simple.php - Pour copier-coller rapidement

$exclude = ['node_modules', '.git', 'vendor', 'logs', 'tmp', 'arbo.txt', 'arbo.php', 'arbo.py', 'arbo.bat', 'bootstrap', 'TEMPLATE_LAYOUT','templateOLD','fonts','tests','webfonts'];
$output = 'arbo.txt';

$h = fopen($output, 'w');
function scan($dir, $exclude, $depth=0, $h) {
    $items = array_diff(scandir($dir), ['.', '..']);
    foreach ($items as $item) {
        $path = $dir . '/' . $item;
        if (is_dir($path) && !in_array($item, $exclude)) {
            fwrite($h, str_repeat('  ', $depth) . '📁 ' . $item . "\n");
            scan($path, $exclude, $depth+1, $h);
        } elseif (!is_dir($path)) {
            fwrite($h, str_repeat('  ', $depth) . '📄 ' . $item . "\n");
        }
    }
}

// Corrigé à 1 cran au-dessus (au lieu de 2)
$targetDir = dirname(__DIR__);

fwrite($h, "Arborescence du dossier : " . $targetDir . "\n");
scan($targetDir, $exclude, 0, $h);
fclose($h);

echo "Fichier '$output' créé !\n";
?>