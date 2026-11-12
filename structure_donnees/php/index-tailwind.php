<?php
// index-tailwind.php
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Web Layout - Tailwind</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>

    <!-- HEADER -->
    <header class="bg-gray-900 text-white text-center p-6">
        <h1 class="text-2xl font-bold">HEADER</h1>
    </header>

    <!-- MAIN CONTAINER -->
    <div class="grid grid-cols-1 md:grid-cols-4 min-h-screen">

        <!-- NAVIGATION -->
        <nav class="bg-gray-100 p-6">
            <h2 class="text-xl font-bold mb-4">NAV</h2>

            <ul class="space-y-3">
                <li>
                    <a href="#" class="text-blue-600 hover:text-blue-800">Link 1</a>
                </li>
                <li>
                    <a href="#" class="text-blue-600 hover:text-blue-800">Link 2</a>
                </li>
                <li>
                    <a href="#" class="text-blue-600 hover:text-blue-800">Link 3</a>
                </li>
                <li>
                    <a href="#" class="text-blue-600 hover:text-blue-800">Link 4</a>
                </li>
                <li>
                    <a href="#" class="text-blue-600 hover:text-blue-800">Link 5</a>
                </li>
            </ul>
        </nav>

        <!-- CONTENT -->
        <main class="md:col-span-2 bg-white p-6">
            <h2 class="text-xl font-bold">CONTENT</h2>
        </main>

        <!-- ASIDE -->
        <aside class="bg-gray-100 p-6">
            <h2 class="text-xl font-bold">ASIDE</h2>
        </aside>

    </div>

    <!-- FOOTER -->
    <footer class="bg-gray-900 text-white text-center p-6">
        <h2 class="text-xl font-bold">FOOTER</h2>
    </footer>

</body>
</html>