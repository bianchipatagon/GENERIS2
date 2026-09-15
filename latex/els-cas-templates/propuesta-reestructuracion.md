# Propuesta de reestructuración — cas-dc-template.tex

## 1. Estructura actual

```
2. Methodology
   2.1 Case study
   2.2 Modelling approach
   2.3 Demand
   2.4 Power supply
       2.4.1 Alternative hydro operation scheme
       2.4.2 Endogenous battery capacity addition

3. Results
   3.1 Demand
   3.2 Power supply
       3.2.1 Regional power generation and trade projections
   3.3 Energy curtailment
```

## 2. Problemas detectados

### 2.1 Asimetría entre Metodología y Resultados

En Metodología, el esquema alternativo de despacho hidroeléctrico y las baterías
están anidados como sub-subsecciones de "Power supply" (2.4.1 y 2.4.2) — es decir,
al mismo nivel que un detalle técnico más del suministro eléctrico.

En Resultados, en cambio, el curtailment aparece como subsección de **primer nivel**
(3.3), al mismo rango jerárquico que Demand (3.1) y Power supply (3.2).

Esto genera una asimetría: el lector espera que la jerarquía de Metodología anticipe
la de Resultados (como sí ocurre con Demand → Demand y, en parte, Power supply →
Power supply), pero el curtailment "aparece" en Resultados sin un correlato de
mismo nivel en Metodología.

### 2.2 Sección 3.2.1 sobrecargada

"Regional power generation and trade projections" (líneas 407–456 del .tex) es,
por lejos, la subsección más extensa del paper: narra, región por región y año
por año (2030/2040/2050), los flujos de importación/exportación para cuatro
escenarios (BAU, BAU-DS, ALT, ALT-DS). Es rigurosa pero muy densa — un lector no
especializado difícilmente retiene el detalle sin apoyarse constantemente en las
figuras.

## 3. Estructura propuesta

```
2. Methodology
   2.1 Case study
   2.2 Modelling approach
   2.3 Demand
   2.4 Power supply
   2.5 Curtailment mitigation strategies      <-- NUEVA subsección de 1er nivel
       2.5.1 Alternative hydro operation scheme
       2.5.2 Endogenous battery capacity addition

3. Results
   3.1 Demand
   3.2 Power supply
       3.2.1 Regional power generation and trade projections   <-- condensada
   3.3 Energy curtailment
```

### Cambios concretos

1. **Promover 2.4.1 y 2.4.2 a subsección propia (2.5).**
   Solo requiere renombrar el nivel del comando LaTeX:
   `\subsubsection{Alternative hydro operation scheme}` (línea 335) y
   `\subsubsection{Endogenous battery capacity addition}` (línea 339)
   pasarían a `\subsection{...}`, con un `\subsection{Curtailment mitigation
   strategies}` opcional como intro breve antes de ambas (o directamente dos
   `\subsection` consecutivas sin padre común, ya que Results 3.3 tampoco las
   subdivide formalmente).

   *Efecto:* el índice queda simétrico — cada subsección de resultados
   (Demand / Power supply / Curtailment) tiene su contraparte metodológica
   explícita del mismo rango.

2. **Condensar 3.2.1.**
   Opciones (no excluyentes):
   - Reescribir los tres párrafos de BAU/BAU-DS (líneas 411–427) como una
     síntesis de 1–2 párrafos que describa el *patrón general* (quién exporta,
     quién importa, cómo evoluciona 2030→2050), remitiendo el detalle
     hora-por-hora únicamente a las figuras (\ref{tradeB}, \ref{inputBAU}).
   - Aplicar el mismo tratamiento a ALT/ALT-DS (líneas 435–450).
   - Considerar una tabla-resumen (región × escenario × rol neto
     exportador/importador por período) como complemento visual, reduciendo la
     necesidad de narrar cada franja horaria en prosa.
   - Si el detalle completo se considera valioso para trazabilidad/revisión,
     moverlo a material suplementario y dejar en el cuerpo principal solo la
     síntesis.

## 4. Trade-off

- **A favor de reestructurar:** mejora la legibilidad y la paridad
  Metodología↔Resultados, que suele ser lo primero que un revisor evalúa al
  hojear el índice.
- **En contra / costo:** condensar 3.2.1 implica decidir qué detalle se
  sacrifica o se manda a suplementario — es trabajo editorial, no solo
  reordenar encabezados, y afecta directamente las figuras que hoy acompañan
  párrafo por párrafo esa narración.

## 5. Siguiente paso sugerido

Si están de acuerdo con el punto 3.1 (promover 2.4.1/2.4.2), es un cambio
mecánico y de bajo riesgo que puedo aplicar directamente al .tex. El punto 3.2
(condensar 3.2.1) conviene discutirlo con los coautores antes de tocar el
texto, ya que implica decisiones de contenido, no solo de forma.
