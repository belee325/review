# python3

# python3
import heapq
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
        next_free_time = [(x, 0) for x in range(self.num_workers)]
        #heapq.heapify(next_free_time)
        for i in range(len(self.jobs)):
            #print(next_free_time)
            self.assigned_workers[i] = next_free_time[0][0]
            self.start_times[i] = next_free_time[0][1]
            next_free_time[0] = (next_free_time[0][0],next_free_time[0][1] + self.jobs[i])
            #heapq.heapify(next_free_time)
            JobQueue.sift_down(next_free_time, 0)
            #print("swapped",next_free_time)
    def sift_down(arr, idx):
            min_idx = idx
            left = 2 * idx + 1
            right = left + 1
            if left < len(arr) and (arr[left][1]<arr[min_idx][1]  or (arr[min_idx][1] == arr[left][1] and
                                                                      arr[min_idx][0] > arr[left][0])):
                min_idx = left
            if right < len(arr) and (arr[right][1]<arr[min_idx][1]  or (arr[min_idx][1] == arr[right][1] and
                                                                      arr[min_idx][0] > arr[right][0])):
                min_idx = right
            if min_idx != idx:
                arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
                JobQueue.sift_down(arr, min_idx)
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()
        
if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
