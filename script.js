const genreOptions = {
  books: ["Fantasy", "Mystery", "Romance", "Science Fiction"],
  movies: ["Action", "Comedy", "Drama", "Horror"],
  tv: ["Sitcom", "Reality", "Thriller", "Documentary"]
};

const categorySelect = document.getElementById("categories");
const genreContainer = document.getElementById("genre-container");

categorySelect.addEventListener("change", () => {
  const selectedCategories = Array.from(categorySelect.selectedOptions).map(
    (opt) => opt.value
  );

  genreContainer.innerHTML = "";

  selectedCategories.forEach((cat) => {
    const label = document.createElement("label");
    label.textContent = `Select ${cat.toUpperCase()} Genres:`;
    genreContainer.appendChild(label);

    genreOptions[cat].forEach((genre) => {
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = `${cat}-genres`;
      checkbox.value = genre;

      const span = document.createElement("span");
      span.textContent = genre;

      const div = document.createElement("div");
      div.appendChild(checkbox);
      div.appendChild(span);

      genreContainer.appendChild(div);
    });
  });
});

document.getElementById("interest-form").addEventListener("submit", (e) => {
  e.preventDefault();

  const selectedCategories = Array.from(categorySelect.selectedOptions).map(
    (opt) => opt.value
  );

  const selectedGenres = {};

  selectedCategories.forEach((cat) => {
    const checkboxes = document.querySelectorAll(
      `input[name="${cat}-genres"]:checked`
    );
    selectedGenres[cat] = Array.from(checkboxes).map((c) => c.value);
  });

  console.log("Selected Interests:", {
    categories: selectedCategories,
    genres: selectedGenres
  });

  alert("Preferences saved!");
});
