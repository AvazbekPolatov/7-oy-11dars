document.addEventListener("DOMContentLoaded", function() {
    let colors = ["#f0f0f0", "#e3f2fd", "#ffebee", "#f3e5f5", "#e8f5e9"];
    let index = 0;

    setInterval(() => {
        document.body.style.background = colors[index];
        index = (index + 1) % colors.length;
    }, 5000); // 5 soniyada fon o‘zgaradi
});

document.getElementById("price-slider").addEventListener("input", function() {
    let maxPrice = this.value;
    document.getElementById("price-label").innerText = "Max Price: $" + maxPrice;

    fetch(`/filter-products?max_price=${maxPrice}`)
        .then(response => response.json())
        .then(data => {
            let productContainer = document.getElementById("product-list");
            productContainer.innerHTML = ""; // Eski mahsulotlarni o‘chirish
            data.products.forEach(product => {
                productContainer.innerHTML += `
                    <div class="product-card">
                        <img src="${product.image}" alt="${product.name}">
                        <h3>${product.name}</h3>
                        <p><del>$${product.old_price}</del> <strong>$${product.new_price}</strong></p>
                        <button class="buy-now">Buy Now</button>
                    </div>
                `;
            });
        });
});

document.querySelectorAll(".heart-icon").forEach(icon => {
    icon.addEventListener("click", function() {
        this.classList.toggle("active"); // CSS bilan qizil qilish
    });
});
