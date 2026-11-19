document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("petal-canvas");
    const ctx = canvas.getContext("2d");

    let width, height;
    let particles = [];
    const particleCount = 50; // Increased count slightly for a fuller effect

    const emojis = ["❤️", "🌹", "💖", "🌸", "🥀", "❤️"]; 
    
    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    class Particle {
        constructor() {
            this.reset();
            this.y = Math.random() * height; 
            this.x = Math.random() * width;
        }

        reset() {
            this.x = Math.random() * width;
            this.y = -40;
            
            this.size = Math.random() * 15 + 20; 
            
            // --- SPEED CHANGES HERE ---
            this.speedY = Math.random() * 2.5 + 1.0;  // Much faster falling speed
            this.speedX = Math.random() * 4 - 2;      // Wider horizontal drift
            // ---------------------------
            
            this.rotation = Math.random() * Math.PI * 2;
            this.rotationSpeed = (Math.random() - 0.5) * 0.1; // Faster spinning
            
            this.wobble = Math.random() * Math.PI * 2;
            this.wobbleSpeed = Math.random() * 0.1 + 0.05; // Faster swirling
            
            this.emoji = emojis[Math.floor(Math.random() * emojis.length)];
            this.opacity = Math.random() * 0.5 + 0.4; 
        }

        update() {
            this.y += this.speedY;
            this.wobble += this.wobbleSpeed;
            
            // Faster, wider side-to-side movement
            this.x += this.speedX + Math.sin(this.wobble) * 2.5; 
            
            this.rotation += this.rotationSpeed;

            // Reset when off screen
            if (this.y > height + 50 || this.x < -50 || this.x > width + 50) {
                this.reset();
            }
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation);
            
            ctx.globalAlpha = this.opacity;
            ctx.font = `${this.size}px serif`;
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            
            ctx.fillText(this.emoji, 0, 0);
            
            ctx.restore();
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        requestAnimationFrame(animate);
    }

    animate();
});