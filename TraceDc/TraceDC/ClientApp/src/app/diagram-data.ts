export interface DiagramData {
  categories: Category[];
}

export interface Category {
  label: string;
  data: Pair[];
}

export interface Pair {
  x: Date | string;
  y: number;
}
