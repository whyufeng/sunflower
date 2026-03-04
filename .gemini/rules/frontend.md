# Frontend Coding Rules (React/Vite)

- **Framework**: Use React with Vite as the build tool.
- **Components**: Use functional components with hooks (`useState`, `useEffect`, etc.).
- **Styling**: 
    - Priority: Modern Vanilla CSS with a focus on premium aesthetics (gradients, glassmorphism, smooth transitions).
    - Use responsive design principles (flexbox/grid).
- **TypeScript**: Use TypeScript (TSX) for better type safety and developer experience.
- **State Management**: Use React Context or standard hooks for simple state. For complex global state, suggest a library (e.g., Zustand).
- **Accessibility (A11y)**: Ensure all interactive elements have labels and are keyboard-navigable.
- **Naming Convention**: 
    - Components: PascalCase (e.g., `Button.tsx`).
    - Utilities/Hooks: camelCase (e.g., `useAuth.ts`).
- **Project Structure**:
    - `src/components/`: Reusable primitive components.
    - `src/features/`: Feature-based logic and components.
    - `src/assets/`: Images, icons, and global styles.
    - `src/App.tsx`: Main application entry.
