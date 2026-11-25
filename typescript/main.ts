export function read(payload: unknown) {
  return [{ stream: "users", data: { id: 1, revision: 1, runtime: "typescript" } }];
}
