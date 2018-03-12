# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [[x,0] for x in range(self.num_workers)]
        for i in range(len(self.jobs)):
            next_worker = next_free_time[0]
            self.assigned_workers[i] = next_worker[0]
            self.start_times[i] = next_worker[1]
            next_worker[1] += self.jobs[i]
            next_free_time[0],next_free_time[self.num_workers-1] = next_free_time[self.num_workers-1],next_free_time[0]
            self.sift_up(next_free_time)
    def sift_up(self,next_free_time):
        for i in reversed(range(0,(self.num_workers)//2)):
            while True:
                min_idx = i
                left = 2*i + 1
                right = left+1
                if left < (self.num_workers) and next_free_time[min_idx][1] >= next_free_time[left][1]:
                    min_idx = left
                if right < (self.num_workers) and next_free_time[min_idx][1] >= next_free_time[right][1]:
                    min_idx = right
                if (left < (self.num_workers) and right <(self.num_workers) and
                    next_free_time[right][1] ==next_free_time[left][1] and next_free_time[min_idx][1] >= next_free_time[right][1] and
                   next_free_time[min_idx][1] >= next_free_time[left][1]):
                    # case where we need to pick from the index number
                    if next_free_time[left][0] <= next_free_time[right][0]:
                        min_idx = left
                    else:
                        min_idx = right
                if min_idx != i:
                    next_free_time[min_idx], next_free_time[i] = next_free_time[i], next_free_time[min_idx]
                    i = min_idx
                else:
                    break
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

