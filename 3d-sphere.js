// Initialize Three.js components
let scene, camera, renderer, sphere, glowSphere;
let mouseX = 0, mouseY = 0;
let windowHalfX = window.innerWidth / 2;
let windowHalfY = window.innerHeight / 2;

// Initialize the application
function init() {
    // Create scene
    scene = new THREE.Scene();
    
    // Create camera
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;
    
    // Create renderer
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    document.body.appendChild(renderer.domElement);
    
    // Create sphere geometry
    const geometry = new THREE.SphereGeometry(2, 32, 32);
    
    // Create main sphere material
    const material = new THREE.MeshPhongMaterial({ 
        color: 0x00aaff,
        emissive: 0x0066cc,
        shininess: 90,
        specular: 0x00aaff
    });
    
    // Create sphere mesh
    sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);
    
    // Create glowing effect with a larger sphere
    const glowMaterial = new THREE.MeshBasicMaterial({
        color: 0x00aaff,
        transparent: true,
        opacity: 0.25,
        blending: THREE.AdditiveBlending
    });
    
    glowSphere = new THREE.Mesh(
        new THREE.SphereGeometry(2.1, 32, 32),
        glowMaterial
    );
    sphere.add(glowSphere);
    
    // Add ambient light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    
    // Add directional light
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);
    
    // Add point light for additional glow
    const pointLight = new THREE.PointLight(0x00aaff, 2, 100);
    pointLight.position.set(0, 0, 0);
    sphere.add(pointLight);
    
    // Add event listeners for mouse movement
    document.addEventListener('mousemove', onDocumentMouseMove);
    
    // Handle window resize
    window.addEventListener('resize', onWindowResize);
}

// Handle mouse movement
function onDocumentMouseMove(event) {
    mouseX = (event.clientX - windowHalfX) / 100;
    mouseY = (event.clientY - windowHalfY) / 100;
}

// Handle window resize
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    
    // Rotate sphere
    sphere.rotation.x += 0.005;
    sphere.rotation.y += 0.005;
    
    // Make sphere respond to mouse movements
    sphere.rotation.x += mouseY * 0.001;
    sphere.rotation.y += mouseX * 0.001;
    
    // Pulsing glow effect
    const scale = 1 + Math.sin(Date.now() * 0.005) * 0.05;
    glowSphere.scale.set(scale, scale, scale);
    
    renderer.render(scene, camera);
}

// Start the application
init();
animate();