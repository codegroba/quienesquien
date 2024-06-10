# Quién es quién

Programado en python y prolog.

## 1. Optimización vs búsqueda.

Un algoritmo de búsqueda se utiliza cuando necesitamos llegar a una solución, en una búsqueda el camino es parte de la solución. En la optimización no importa el camino a la solución sinó que dicha solución sea aceptable independientemente del camino.

## 2. Entorno del agent.

| Entorno de tareas | Completa / parcialmente observable | Agentes    | Determinista / Estocástico | Episodico / Secuencial | Estático / Dinámico | Discreto |
| ----------------- | ---------------------------------- | ---------- | -------------------------- | ---------------------- | ------------------- | -------- |
| Q e q             | Parcialmente                       | Individual | Estocástico                | Secuencial             | Estático            | Discreto |

## 3. Algoritmo.

He elegido un algoritmo de optimización "voraz". El planteamiento es que dados los personajes que sigan en el juego y no han sido descartados, vamos a buscar cual de las preguntas de las que disponemos va a descartar el número de personajes mas cercano a la mitad de los que siguen en juego.

## 4. Agente.

![](/home/cristian/CursoIA/MIA/Qeq/Axente.png)

## 5. Programación lógica.

La programación lógica no aborda los problemas entorno al cómo sinó al qué, se trabaja de forma descriptiva, estableciendo relaciones entre entidades. Este paradigma se basa en la fórmula "algoritmos = lógica + control" (ecuación informal de Kowalski), lo que significa que un algoritmo especifica el conocimiento mediante axiomas (lógica) y el problema se resuelve mediante un mecanismo de inferencia que actúa soble el mismo (control).

El "quién es quién" es un problema adecuado para resolverlo con Prolog dado que creando reglas podemos acceder al conocimiento de manera muy eficiente. Con otro tipo de programación sería un trabajo mas grande tanto de progamación como computación. De esta manera también evitamos problemas de backtraking.

## 6. Base de datos Prolog.

Representamos el conocimiento de la siguiente forma:

```
`personaje(herman / [hombre, pelirrojo, calva, nariz_grande, ojos_marrones, cejas_gruesas]).`
```

Cada personaje tiene un nombre y sus características. En prolog con una simple consulta podremos saber que personajes tienen cierta característica.

```
personaje(Nombre / Caracteristicas)
```

De esta manera tanto la programación como el acceso al conocimiento es muy simple.
