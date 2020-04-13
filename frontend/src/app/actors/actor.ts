import { Agent } from '../agents/agent';
import { Movie } from '../movies/movie';
export interface Actor {
  id: number;
  name: string;
  age: number;
  gender: string;
  headshot_url: string;
  agent_id: number;
  agent: Agent;
  movies: Movie[];
}
