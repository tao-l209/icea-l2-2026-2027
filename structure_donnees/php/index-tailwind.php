<?php
// index-tailwind.php
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>MyWebsite - Tailwind</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>

<body class="bg-gray-100 min-h-screen">

    <!-- HEADER -->
    <header class="bg-gray-900 text-white p-4">

        <div class="flex items-center justify-between flex-wrap gap-4">

            <!-- SITE NAME -->
            <div>
                <a href="#" class="text-2xl font-bold text-white no-underline">
                    MyWebsite
                </a>
            </div>


            <!-- NAVIGATION -->
            <nav>
                <ul class="flex items-center flex-wrap gap-6">

                    <li>
                        <a href="#" class="text-white hover:text-blue-400">
                            Home
                        </a>
                    </li>

                    <li>
                        <a href="#" class="text-white hover:text-blue-400">
                            About
                        </a>
                    </li>

                    <li>
                        <a href="#" class="text-white hover:text-blue-400">
                            Services
                        </a>
                    </li>

                    <li>
                        <a href="#" class="text-white hover:text-blue-400">
                            Contact
                        </a>
                    </li>

                </ul>
            </nav>


            <!-- LOGIN / PASSWORD -->
            <div>

                <form class="flex flex-wrap items-center gap-2">

                    <input
                        type="text"
                        placeholder="Login"
                        class="w-32 rounded-md border border-gray-600 bg-white px-3 py-2 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                    >

                    <input
                        type="password"
                        placeholder="Password"
                        class="w-32 rounded-md border border-gray-600 bg-white px-3 py-2 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                    >

                    <button
                        type="button"
                        class="rounded-md bg-blue-600 px-4 py-2 font-semibold text-white hover:bg-blue-700"
                    >
                        Login
                    </button>

                </form>

            </div>


            <!-- LANGUAGE -->
            <div>

                <select class="rounded-md border border-gray-600 bg-gray-800 px-3 py-2 text-white">

                    <option>FR</option>
                    <option>EN</option>
                    <option>ES</option>

                </select>

            </div>

        </div>

    </header>


    <!-- MAIN CONTAINER -->
    <div class="grid grid-cols-1 gap-6 p-6 md:grid-cols-3">


        <!-- CONTENT -->
        <main class="rounded-lg bg-white p-6 shadow-sm md:col-span-2">

            <h2 class="mb-4 text-2xl font-bold text-gray-900">
                CONTENT
            </h2>

            <p class="text-gray-600">
                Welcome to MyWebsite.
                This is the main content section.
            </p>

        </main>


        <!-- ASIDE -->
        <aside class="rounded-lg bg-white p-6 shadow-sm">

            <h2 class="mb-4 text-2xl font-bold text-gray-900">
                ASIDE
            </h2>

            <p class="text-gray-600">
                Additional information goes here.
            </p>

        </aside>


    </div>


    <!-- FOOTER -->
    <footer class="mt-4 bg-gray-900 p-6 text-center text-white">

        <p>
            © 2026 MyWebsite - All rights reserved.
        </p>

    </footer>

</body>
</html>