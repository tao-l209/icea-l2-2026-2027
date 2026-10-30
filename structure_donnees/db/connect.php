<?php
/**
 * db/connect.php
 * Connexion PDO à la base icea-l2-2026-2027 (localhost)
 */

// --- Configuration ---
$host    = '127.0.0.1';               // ou 'localhost'
$port    = 3306;
$dbname  = 'icea-l2-structure-donnees';
$user    = 'root';
$pass    = '';                        // à adapter (XAMPP/WAMP: souvent vide)
$charset = 'utf8mb4';

// --- DSN ---
$dsn = "mysql:host=$host;port=$port;dbname=$dbname;charset=$charset";

// --- Options PDO ---
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

// --- Connexion ---
try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (PDOException $e) {
    // En prod : log l'erreur, ne pas l'afficher
    http_response_code(500);
    die("Erreur de connexion à la base de données : " . $e->getMessage());
}