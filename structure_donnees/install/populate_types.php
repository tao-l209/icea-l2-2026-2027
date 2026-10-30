<?php
/**
 * structure_donnees/install/populate_types.php
 * Insère les types d'utilisateurs : admin, superviseur, client, guest
 * Base de données : icea-l2-2026-2027
 */

// --- Connexion partagée ---
require_once __DIR__ . '/../db/connect.php'; // expose $pdo

// --- Types à insérer ---
$types = ['admin', 'superviseur', 'client', 'guest'];

// --- Insertion idempotente (pas de doublons) ---
try {
    $stmtCheck  = $pdo->prepare("SELECT COUNT(*) FROM `types` WHERE `title` = :title");
    $stmtInsert = $pdo->prepare("INSERT INTO `types` (`title`) VALUES (:title)");

    $inserted = 0;
    $skipped  = 0;

    foreach ($types as $type) {
        $stmtCheck->execute([':title' => $type]);
        if ($stmtCheck->fetchColumn() == 0) {
            $stmtInsert->execute([':title' => $type]);
            $inserted++;
            echo "✔ Type ajouté : $type\n";
        } else {
            $skipped++;
            echo "↷ Type déjà présent : $type\n";
        }
    }

    echo "\nTerminé. $inserted ajouté(s), $skipped ignoré(s).\n";

} catch (PDOException $e) {
    die("Erreur lors de l'insertion : " . $e->getMessage());
}