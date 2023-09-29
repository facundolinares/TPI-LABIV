class Estudiante {
    constructor() {
        this.nombre = this.generarNombreAleatorio();
        this.edad = this.generarEdadAleatoria();
        this.calificaciones = this.generarCalificacionesAleatorias();
    }

    generarNombreAleatorio() {
        const nombres = ["Juan", "María", "Carlos", "Laura", "Andrés", "Sofía"];
        const apellido = ["Pérez", "Gómez", "López", "Fernández", "Martínez", "Rodríguez"];
        const nombreAleatorio = nombres[Math.floor(Math.random() * nombres.length)];
        const apellidoAleatorio = apellido[Math.floor(Math.random() * apellido.length)];
        return `${nombreAleatorio} ${apellidoAleatorio}`;
    }

    generarEdadAleatoria() {
        return Math.floor(Math.random() * 10) + 18; // Edades entre 18 y 27 años
    }

    generarCalificacionesAleatorias() {
        const calificaciones = [];
        for (let i = 0; i < 5; i++) {
            calificaciones.push(Math.floor(Math.random() * 51) + 50); // Calificaciones entre 50 y 100
        }
        return calificaciones;
    }

    calcularPromedio() {
        if (this.calificaciones.length === 0) {
            return 0;
        }

        const sumaCalificaciones = this.calificaciones.reduce((total, calificacion) => total + calificacion, 0);
        return sumaCalificaciones / this.calificaciones.length;
    }

    mostrarInformacion() {
        console.log(`Nombre: ${this.nombre}`);
        console.log(`Edad: ${this.edad}`);
        console.log(`Calificaciones: ${this.calificaciones.join(', ')}`);
        console.log(`Promedio de Calificaciones: ${this.calcularPromedio()}`);
    }
}

// Crear una instancia de la clase Estudiante con datos aleatorios
const estudiante = new Estudiante();

// Mostrar la información del estudiante generado aleatoriamente
estudiante.mostrarInformacion();